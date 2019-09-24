import sys
import pygame
import pygame.camera
import time
import random
import logging
import os
import lib.cc_configuration as gameConfig
from lib.cc_gtext import cc_gtext
from lib.cc_guielem import cc_guielem
from lib.cc_udpclient import cc_udpclient
from lib.cc_cameras import cc_cameras

os.environ['SDL_AUDIODRIVER'] = 'dsp' # alsa driver error issue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
udpClient = cc_udpclient()

clock = pygame.time.Clock()
pygame.init() 
pygame.mixer.quit()  #performance work around - not needed normally
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
pygame.display.set_caption('Steer the Car')

gText = cc_gtext(screen)
guiElem = cc_guielem(screen)
cameras = cc_cameras(screen)

pressedXcounter = 0
throttlePressedCounter = 0
direction = 0
throttle = 0
headlights = 0
hudRendering = 1

DIR_MAX_POSITION = 5
DIR_MIN_POSITION = -5
THR_FORWARD_MAX = 1
THR_BACKWARD_MAX = -1

def direction_decrease(dirvalue):
    if dirvalue > DIR_MIN_POSITION:
        dirvalue = dirvalue-1
        udpClient.sendPWM('dir',dirvalue)
    return dirvalue
        
def direction_increase(dirvalue):
    if dirvalue < DIR_MAX_POSITION:
        dirvalue = dirvalue+1
        udpClient.sendPWM('dir',dirvalue)
    return dirvalue

def throttle_increase():
    udpClient.sendPWM('thr',1)

def throttle_decrease():
    udpClient.sendPWM('thr',-1)
    
def enable_headlights(headl):
    return_value = 0
    if headl > 0:
        udpClient.sendPWM('headl',0)
    else:
        udpClient.sendPWM('headl',1)
        return_value = 1
    return return_value

def enable_hudRendering(hudr):
    return_value = 0
    if hudr == 0:
        return_value = 1
    elif hudr == 1:
        return_value = 2
    elif hudr == 2:
        return_value = 0      
    return return_value

def render_hud():
    sensors = udpClient.fetchSensors('ALL')
    guiElem.modelHorizonScale(1,2)
    guiElem.modelHorizonLine(180, 240, sensors['accel']['x'], sensors['accel']['y'], sensors['accel']['z'])
    #guiElem.modelHorizonLine(180, 240, 0, 0, 0)

    guiElem.modelHorizonValues(330, 100, sensors['accel']['x'],sensors['accel']['y'],sensors['accel']['z'])
    guiElem.modelWheelsState(1, 2, direction, throttle)
    guiElem.modelGeneralMetrics(80, 100, 8.40, 5.11, 3.21, sensors['system']['core_temp'])
    guiElem.modelBatteryLevel(150, 5, 8.40)

    #render_horizon(-1.7860744384765623,-9.016563452148437,2.205059729003906)

crashed = False

while not crashed:
    time.sleep(0.001)
    timeNow = pygame.time.get_ticks()
    cameras.modelFrontCameraView()
    if hudRendering:
        cameras.modelBackCameraView()
    if hudRendering == 2:          
        render_hud()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          cameras.stopCameras()
          crashed = True
          pygame.quit()
          sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = direction_decrease(direction)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = direction_increase(direction)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                throttlePressedCounter = pygame.time.get_ticks()
                if throttle < 1:
                   throttle_increase()
                   throttle = 1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                throttlePressedCounter = pygame.time.get_ticks()               
                if throttle > -1:
                   throttle_decrease()
                   throttle = -1                              
            if event.key == pygame.K_v:
                hudRendering = enable_hudRendering(hudRendering)             
            if event.key == pygame.K_h:
                udpClient.sendPWM('horn',1)                
            if event.key == pygame.K_h:
                udpClient.sendPWM('horn',1)
            if event.key == pygame.K_f:
                udpClient.sendPWM('headlblink',1)
            if event.key == pygame.K_g:
                headlights = enable_headlights(headlights)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                pressedXcounter = 0
            if event.key == pygame.K_h:
                udpClient.sendPWM('horn',0)
            if event.key == pygame.K_f:
                udpClient.sendPWM('headlblink',0)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pressedXcounter = pressedXcounter+1
        if pressedXcounter > 1:
            pressedXcounter = 0
            direction = direction_decrease(direction)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pressedXcounter = pressedXcounter+1
        if pressedXcounter > 1:   
            pressedXcounter = 0
            direction = direction_increase(direction)

    if timeNow - gameConfig.KEEP_THROTTLE_PRESSED_MS > throttlePressedCounter:
        if throttle != 0:
            udpClient.sendPWM('thr',0)
            throttle = 0

    pygame.time.wait(0)
    #pygame.display.update()
    clock.tick(25)

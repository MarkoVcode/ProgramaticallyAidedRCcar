#!/usr/bin/python3
import sys
import pygame
import time
import random
import logging
import os
import lib.cc_configuration as gameConfig
from lib.cc_gatext import cc_gatext
from lib.cc_guielem import cc_guielem
from lib.cc_udpclient import cc_udpclient
from lib.cc_cameras import cc_cameras
from lib.cc_control import cc_control
from lib.cc_sensors import cc_sensors

os.environ['SDL_AUDIODRIVER'] = 'dsp' # alsa driver error issue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
udpClient = cc_udpclient()

clock = pygame.time.Clock()
pygame.init() 
pygame.mixer.quit()  #performance work around - not needed normally
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

#https://stackoverflow.com/questions/29135147/what-do-hwsurface-and-doublebuf-do
screen = pygame.display.set_mode((640,480),0)
pygame.display.set_caption('Steer the Car')

animText = cc_gatext(screen)
guiElem = cc_guielem(screen)
cameras = cc_cameras(screen)
control = cc_control(udpClient)

def render_hud():
    sensors = udpClient.fetchSensors('ALL')
    guiElem.modelHorizonScale(1,2)
    if udpClient.isConnectionAlive():
        guiElem.modelWheelsState(1, 2, control.getDirection(), control.getThrottle())
        guiElem.modelRoadOutline(0, 240, control.getDirection())
        if 'accel' in sensors.keys():
            guiElem.modelHorizonLine(180, 240, sensors['accel_flt']['x'], sensors['accel_flt']['y'], sensors['accel_flt']['z'])
            guiElem.modelHorizonValues(330, 100, sensors['accel_flt']['x'],sensors['accel_flt']['y'],sensors['accel_flt']['z'])
        if 'power' in sensors.keys():
            guiElem.modelPowerMetrics(80, 100, round(sensors['power_flt']['battery_volt'],1), round(sensors['power_flt']['pi_volt'],1), round(sensors['power_flt']['pi_current'],1))
            guiElem.modelBatteryLevel(150, 5, 330, sensors['power_flt']['battery_volt'], gameConfig.BATTERY_VOLTAGE_MIN, gameConfig.BATTERY_VOLTAGE_MAX, gameConfig.BATTERY_VOLTAGE_WARN, gameConfig.BATTERY_VOLTAGE_CRIT)
        if 'system' in sensors.keys():
            guiElem.modelSystemMetrics(80, 140, round(sensors['system_flt']['core_temp'], 1))
       #guiElem.modelHorizonLine(180, 240, 0, 0, 0)
       #render_horizon(-1.7860744384765623,-9.016563452148437,2.205059729003906)

crashed = False
zoom = False
while not crashed:
    time.sleep(0.001)
    cameras.modelFrontCameraView()
    guiElem.modelRadar(20, 400)
    if control.getHudRendering():
        #cameras.modelBackCameraView()
        cameras.modelAnimatedBackCameraView(zoom)
    if control.getHudRendering() == 2:          
        render_hud()
    if not udpClient.isConnectionAlive():
        animText.pulseText(320,75, "Lost connection with devices server!")

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
            if event.key == pygame.K_m:
                zoom = True 
            if event.key == pygame.K_n:
                cameras.rotateCameraList()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_m:
                zoom = False

        control.processKeyboardEvent(event)

    control.processPressedKeys(pygame.key.get_pressed())
    pygame.time.wait(0)
    clock.tick(25)

import sys
import pygame
import pygame.camera
import time
import random
import UDPIOClient
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
udpClient = UDPIOClient.UDPIOClient()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
RED_HIGHLIGHT = (240, 50, 50, 50)

clock = pygame.time.Clock()
pygame.init()
pygame.mixer.quit()  #performance work around - not needed normally
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
pygame.display.set_caption('Steer the Car')
screen_rect = screen.get_rect()

cam_list = pygame.camera.list_cameras()
camBack  = None
camFront = None
if len(cam_list) >= 2:
    camFront = pygame.camera.Camera(cam_list[0],(640,480))
    camBack  = pygame.camera.Camera(cam_list[1],(160,120))
    camFront.start()
    camBack.start()
elif len(cam_list) == 1:
    camFront = pygame.camera.Camera(cam_list[0],(640,480))
    camFront.start()
else: 
    print("No cameras!!")

see_through = pygame.Surface((100,100)).convert_alpha()
see_through.fill(RED_HIGHLIGHT)
see_through_rect = see_through.get_rect(bottomleft=screen_rect.center)

pressedXcounter = 0
direction = 0
throttle = 0
headlights = 0
hudRendering = 1

DIR_MAX_POSITION = 5
DIR_MIN_POSITION = -5
THR_FORWARD_MAX = 1
THR_BACKWARD_MAX = -1

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((640/2),(480/2))
    screen.blit(TextSurf, TextRect)

def direction_decrease(dirvalue):
    if dirvalue > DIR_MIN_POSITION:
        dirvalue = dirvalue-1
        udpClient.sendPWM('dir',dirvalue)
    return dirvalue
        #logging.debug('Awaiting for the messages. ' + str(q.qsize()) + ' items in queue')
        
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
    screen.blit(see_through, see_through_rect)
    message_display("---")

crashed = False

while not crashed:
    time.sleep(0.001)
    if camFront:
        image1 = camFront.get_image()
        image1 = pygame.transform.scale(image1,(720,480))
        screen.blit(image1,(0,0))
    if camBack:
        if hudRendering:
            image2 = camBack.get_image()
            image2 = pygame.transform.scale(image2,(160,120))
            screen.blit(image2,(240,356))
    if hudRendering == 2:          
        render_hud()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          camFront.stop()
          camBack.stop()
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
                throttle_increase()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                throttle_decrease()
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
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                udpClient.sendPWM('thr',0)
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

    pygame.time.wait(0)
    #pygame.display.update()
    clock.tick(25)

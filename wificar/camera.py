import sys
import pygame
import pygame.camera
import time
import random
import UDPIOClient
import logging
import os
import gameConfig

os.environ['SDL_AUDIODRIVER'] = 'dsp' # alsa driver error issue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
udpClient = UDPIOClient.UDPIOClient()

black = (0,0,0)
white = (255,255,255)
RED_HIGHLIGHT = (255, 255, 255, 20)

clock = pygame.time.Clock()
pygame.init() 
pygame.mixer.quit()  #performance work around - not needed normally
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
pygame.display.set_caption('Steer the Car')
screen_rect = screen.get_rect()

cam_list = pygame.camera.list_cameras()
if gameConfig.isHardwareSupported():
    cam_list = ['/dev/video2','/dev/video0']

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

see_through = pygame.Surface((300,300)).convert_alpha()
see_through.fill(RED_HIGHLIGHT)
see_through_rect = see_through.get_rect(center=screen_rect.center)

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

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #largeText = pygame.font.Font('freesansbold.ttf',115)
    largeText = pygame.font.Font('fonts/PixelOperator.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((640/2),(480/2))
    screen.blit(TextSurf, TextRect)

def render_horizon_scale():
    largeText = pygame.font.Font('fonts/PixelOperator.ttf',18)
    blue = 255, 255, 255
#Vertical Lines
    point1 = 160, 120
    point2 = 160, 360
    pygame.draw.line(screen, blue, point1, point2)
    point3 = 480, 120
    point4 = 480, 360
    pygame.draw.line(screen, blue, point3, point4)

#Number Lines Left
    point11 = 150, 120
    point12 = 160, 120
    pygame.draw.line(screen, blue, point11, point12)
    point7 = 150, 240
    point8 = 160, 240
    pygame.draw.line(screen, blue, point7, point8)
    point13 = 150, 360
    point14 = 160, 360
    pygame.draw.line(screen, blue, point13, point14)
    point23 = 155, 180
    point24 = 160, 180
    pygame.draw.line(screen, blue, point23, point24)
    point25 = 155, 300
    point26 = 160, 300
    pygame.draw.line(screen, blue, point25, point26)        

#Number Lines Right
    point15 = 480, 120
    point16 = 490, 120
    pygame.draw.line(screen, blue, point15, point16)
    point9 = 480, 240
    point10 = 490, 240
    pygame.draw.line(screen, blue, point9, point10)
    point17 = 480, 360
    point18 = 490, 360
    pygame.draw.line(screen, blue, point17, point18)
    point19 = 480, 180
    point20 = 485, 180
    pygame.draw.line(screen, blue, point19, point20)
    point21 = 480, 300
    point22 = 485, 300
    pygame.draw.line(screen, blue, point21, point22)

#Numbers Left
    TextSurfMaxL, TextRectMaxL = text_objects('180', largeText)
    TextRectMaxL.center = (136,120)
    TextSurfNeutralL, TextRectNeutralL = text_objects('0', largeText)
    TextRectNeutralL.center = (140,240)
    TextSurfMinL, TextRectMinL = text_objects('180', largeText)
    TextRectMinL.center = (136,360)

    screen.blit(TextSurfNeutralL, TextRectNeutralL)
    screen.blit(TextSurfMaxL, TextRectMaxL)
    screen.blit(TextSurfMinL, TextRectMinL)

#Numbers Right
    TextSurfMaxR, TextRectMaxR = text_objects('180', largeText)
    TextRectMaxR.center = (504,120)
    TextSurfNeutralR, TextRectNeutralR = text_objects('0', largeText)
    TextRectNeutralR.center = (500,240)
    TextSurfMinR, TextRectMinR = text_objects('180', largeText)
    TextRectMinR.center = (504,360)

    screen.blit(TextSurfNeutralR, TextRectNeutralR)
    screen.blit(TextSurfMaxR, TextRectMaxR)
    screen.blit(TextSurfMinR, TextRectMinR)

    pygame.draw.circle(screen, (255,255,255), ((640/2),(480/2)), 2, 1)

def render_horizon(x,y,z):
    x = round(x * 12)
    y = round(y * 12)

    blue = 255, 255, 230
    point5 = 180, (240 + y) +x
    point6 = 460, (240 - y) +x 
    #vert
    #point5 = 320, 120
    #point6 = 320, 360
    #flat
    #point5 = 180, 240
    #point6 = 460, 240
    #maxl
    #point5 = 180, 120
    #point6 = 460, 360
    #minr
    #point5 = 180, 360
    #point6 = 460, 120
    #maxfr
    #point5 = 180, 360
    #point6 = 460, 360
    #maxbk
    #point5 = 180, 120
    #point6 = 460, 120
    pygame.draw.line(screen, blue, point5, point6)

def render_horizon_values(x,y,z):
    xoffset = 330
    yoffset = 100
    largeText = pygame.font.Font('fonts/PixelOperator.ttf',17)
    TextSurfx, TextRectx = text_objects('x:'+str(x), largeText)
    TextRectx.center = (xoffset,yoffset)
    TextSurfy, TextRecty = text_objects('y:'+str(y), largeText)
    TextRecty.center = (xoffset,yoffset + 13)
    TextSurfz, TextRectz = text_objects('z:'+str(z), largeText)
    TextRectz.center = (xoffset,yoffset + 26)

    screen.blit(TextSurfx, TextRectx)
    screen.blit(TextSurfy, TextRecty)
    screen.blit(TextSurfz, TextRectz)

def render_wheels(dirValue, throttleValue):
    xoffset = -30
    yoffset = -200
    blue = 225, 255, 200
    point1 = 600+xoffset, 360+yoffset
    point2 = 600+xoffset, 430+yoffset
    pygame.draw.line(screen, blue, point1, point2, 3)
    point3 = 570+xoffset, 360+yoffset
    point4 = 630+xoffset, 360+yoffset
    pygame.draw.line(screen, blue, point3, point4, 3)
    point5 = 570+xoffset, 430+yoffset
    point6 = 630+xoffset, 430+yoffset
    pygame.draw.line(screen, blue, point5, point6, 3)
    pygame.draw.circle(screen, blue, (600+xoffset,360+yoffset), 5, 1)
    pygame.draw.circle(screen, blue, (600+xoffset,430+yoffset), 5, 1)
    #tyres front
    point9 = 570+dirValue+xoffset, 345+yoffset
    point10 = 570-dirValue+xoffset, 376+yoffset
    pygame.draw.line(screen, blue, point9, point10, 12)
    point11 = 630+dirValue+xoffset, 345+yoffset
    point12 = 630-dirValue+xoffset, 376+yoffset
    pygame.draw.line(screen, blue, point11, point12, 12)
    #tyres back
    point7 = 570+xoffset, 415+yoffset
    point8 = 570+xoffset, 446+yoffset
    pygame.draw.line(screen, blue, point7, point8, 12)
    point13 = 630+xoffset, 415+yoffset
    point14 = 630+xoffset, 446+yoffset
    pygame.draw.line(screen, blue, point13, point14, 12)
    if dirValue == 0:
        point15 = 583+xoffset, 360+yoffset
        point16 = 617+xoffset, 360+yoffset
        pygame.draw.line(screen, blue, point15, point16, 5)
    if throttleValue > 0:
        point17 = 583+xoffset, 350+yoffset
        point18 = 600+xoffset, 340+yoffset
        pygame.draw.line(screen, blue, point17, point18, 4)
        point21 = 600+xoffset, 340+yoffset
        point22 = 617+xoffset, 350+yoffset
        pygame.draw.line(screen, blue, point21, point22, 4)
        point23 = 583+xoffset, 340+yoffset
        point24 = 600+xoffset, 330+yoffset
        pygame.draw.line(screen, blue, point23, point24, 4)
        point25 = 600+xoffset, 330+yoffset
        point26 = 617+xoffset, 340+yoffset
        pygame.draw.line(screen, blue, point25, point26, 4)
    if throttleValue < 0:
        point27 = 583+xoffset, 440+yoffset
        point28 = 600+xoffset, 450+yoffset
        pygame.draw.line(screen, blue, point27, point28, 4)
        point29 = 600+xoffset, 450+yoffset
        point30 = 617+xoffset, 440+yoffset
        pygame.draw.line(screen, blue, point29, point30, 4)
        point31 = 583+xoffset, 450+yoffset
        point32 = 600+xoffset, 460+yoffset
        pygame.draw.line(screen, blue, point31, point32, 4)
        point33 = 600+xoffset, 460+yoffset
        point34 = 617+xoffset, 450+yoffset
        pygame.draw.line(screen, blue, point33, point34, 4)   

def render_electrical_metrics(battVoltage, rpiVoltage, rpiCurr, rpiStabTemp):
    xoffset = 80
    yoffset = 100
    largeText = pygame.font.Font('fonts/PixelOperator.ttf',17)
    TextSurfx, TextRectx = text_objects('Bat: ' + str(battVoltage) + 'V', largeText)
    TextRectx.center = (xoffset,yoffset)
    TextSurfy, TextRecty = text_objects('PI: ' + str(rpiVoltage) + 'V', largeText)
    TextRecty.center = (xoffset,yoffset + 13)
    TextSurfz, TextRectz = text_objects('PI: ' + str(rpiCurr) + 'A', largeText)
    TextRectz.center = (xoffset,yoffset + 26)
    TextSurfh, TextRecth = text_objects('PI: ' + str(rpiStabTemp) + 'C', largeText)
    TextRecth.center = (xoffset,yoffset + 39)

    screen.blit(TextSurfx, TextRectx)
    screen.blit(TextSurfy, TextRecty)
    screen.blit(TextSurfz, TextRectz)
    screen.blit(TextSurfh, TextRecth)

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
    #print(sensors['accel'])
    screen.blit(see_through, see_through_rect)
    render_horizon_scale()
    if gameConfig.isHardwareSupported():
        render_horizon(sensors['accel']['x'],sensors['accel']['y'],sensors['accel']['z'])
        render_horizon_values(sensors['accel']['x'],sensors['accel']['y'],sensors['accel']['z'])
    else:
        render_horizon(-1.7860744384765623,-9.016563452148437,2.205059729003906)
        #render_horizon(-5,-5,0)
        render_horizon_values(-1.7860744384765623,-9.016563452148437,2.205059729003906)
    render_wheels(direction, throttle)
    render_electrical_metrics(8.40, 5.11, 3.21, 40)
    #message_display(".")

crashed = False

while not crashed:
    time.sleep(0.001)
    timeNow = pygame.time.get_ticks()
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

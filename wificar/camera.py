from __future__ import division
import sys
import pygame
import pygame.camera
import time
import random
#import Adafruit_PCA9685
import socket
import sys
import UDPIOClient

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

#pwm = Adafruit_PCA9685.PCA9685()
#pwm.set_pwm_freq(60)
udpClient = UDPClient()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
RED_HIGHLIGHT = (240, 50, 50, 100)

clock = pygame.time.Clock()
pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
screen_rect = screen.get_rect()

cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(512,384))
cam.start()
see_through = pygame.Surface((100,100)).convert_alpha()
see_through.fill(RED_HIGHLIGHT)
see_through_rect = see_through.get_rect(bottomleft=screen_rect.center)

xoffset = 340
yoffset = 350
x_change = xoffset
y_change = yoffset
gameExit = False
pressedXcounter = 0

def send_to_io_server(goal, value):
    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(goal, server_address)
    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((640/2),(480/2))
    screen.blit(TextSurf, TextRect)

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1,(640,480))
    screen.blit(image1,(0,0))
    screen.blit(see_through, see_through_rect)
    message_display("---")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          cam.stop()
          pygame.quit()
          sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_change > 300:
                   x_change = x_change-10
            if event.key == pygame.K_RIGHT:
                if x_change < 380:
                   x_change = x_change+10
            if event.key == pygame.K_UP:
                y_change = yoffset+20
            if event.key == pygame.K_DOWN:
                y_change = yoffset-20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pressedXcounter = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = yoffset

    keys=pygame.key.get_pressed()
    print(pressedXcounter)
    if keys[pygame.K_LEFT]:
        pressedXcounter = pressedXcounter+1
        if pressedXcounter > 1:
            pressedXcounter = 0
            x_change = x_change - 10
    if keys[pygame.K_RIGHT]:
        pressedXcounter = pressedXcounter+1
        if pressedXcounter > 1:   
            pressedXcounter = 0
            x_change = x_change + 10

    #pwm.set_pwm(3, 0, x_change)
    send_to_io_server("pwm_direction", x_change)
    #pwm.set_pwm(2, 0, y_change)
    send_to_io_server("pwm_throttle", y_change)
    print(x_change)
    print(y_change) 

    #pygame.display.update()
    clock.tick(60)
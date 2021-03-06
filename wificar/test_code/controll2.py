from __future__ import division
import pygame
import time
import random
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

#######
#def things(thingx, thingy, thingw, thingh, color):
#    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#######

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    xoffset = 340
    yoffset = 350
    x_change = xoffset
    y_change = yoffset
######
   # thing_startx = random.randrange(0, display_width)
   # thing_starty = -600
   # thing_speed = 7
   # thing_width = 100
   # thing_height = 100
######
    gameExit = False
    pressedXcounter = 0
#    pressedXRcounter = 0
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
#                    pressedXRcounter = 0
               #     if x_change > 380:
               #         x_change = 380
               #     if x_change < 300:
               #         x_change = 300
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = yoffset


#        move_ticker = 0
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


        pwm.set_pwm(3, 0, x_change)
        pwm.set_pwm(2, 0, y_change)
        print(x_change)
        print(y_change) 
        x += x_change
        y += y_change
        gameDisplay.fill(white)


     ##########
        # things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, thing_starty, thing_width, thing_height, black)
        #thing_starty += thing_speed
        car(x-xoffset,y-yoffset)
     ##########
        #if x > display_width - car_width or x < 0:
        #    crash()

        #if thing_starty > display_height:
        #    thing_starty = 0 - thing_height
        #    thing_startx = random.randrange(0,display_width)
            
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()

import sys
import pygame
import pygame.camera

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640,480),0)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(512,384))
cam.start()

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
   message_display("DDDDDDDDDDDD")
   pygame.display.update()

   for event in pygame.event.get():
          if event.type == pygame.QUIT:
              cam.stop()
              pygame.quit()
              sys.exit()

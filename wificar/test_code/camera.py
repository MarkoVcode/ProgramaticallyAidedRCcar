import pygame
import pygame.camera
from pygame.locals import *

SIZEScreen = (640, 480)

DEVICE1 = '/dev/video0'
SIZE1 = (640, 480)
FILENAME1 = 'capture1.png'

DEVICE2 = '/dev/video3'
SIZE2 = (340, 280)
FILENAME2 = 'capture2.png'

def camstream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZEScreen, 0)
    camera1 = pygame.camera.Camera(DEVICE1, SIZE1)
    camera1.start()
    camera2 = pygame.camera.Camera(DEVICE2, SIZE1)
    camera2.start()

    #screen = pygame.surface.Surface(SIZEScreen, 0, display)
    screen = pygame.display.set_mode((640,480),0)

    capture = True
    while capture:
        image1 = camera1.get_image()
        image2 = camera2.get_image()
        image1 = pygame.transform.scale(image1,(640,480))
        image2 = pygame.transform.scale(image2,(340,280))
        screen.blit(image1,(0,0))
        pygame.display.flip()
        screen.blit(image2,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                pygame.image.save(screen, FILENAME1)
    camera1.stop()
    camera2.stop()
    pygame.quit()
    return

if __name__ == '__main__':
    camstream()


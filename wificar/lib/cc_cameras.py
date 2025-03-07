import logging
import lib.cc_configuration as cc_configuration
import pygame
import pygame.camera
from pygame.locals import *
import array

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class cc_cameras:
    def __init__(self, screen, camerasDevices=cc_configuration.CAMERAS_LIST):
        pygame.camera.init()
        self.cam_list = camerasDevices
        self.screen = screen
        self.cameras = []
        self.discoverCameras()

        #For camera zoom animation
        self.backx = 160
        self.backy = 120
        self.backpx = 240
        self.backpy = 356
        self.backDefx = 160
        self.backDefy = 120
        self.backDefpx = 240
        self.backDefpy = 356
        self.backMaxx = 640
        self.backMaxy = 480
        self.backMaxpx = 0
        self.backMaxpy = 0

    def discoverCameras(self):
        i = 0
        while i < len(self.cam_list): 
            try:
                cam = pygame.camera.Camera(self.cam_list[i],(640,480))
                cam.start()
                self.cameras.append(cam)
            except Exception as e:
                logging.debug('Camera init problem: {0}'.format(e))
            i += 1
        print("Discovered cameras: ")
        print(self.cameras)

    def renderAllCameras(self, picSize):
        i = 0
        while i < len(self.cameras):
            if i == 0:
                position = (0,0)
            elif i == 1:
                position = (320,0)
            elif i == 2:
                position = (0,240)
            elif i == 3:
                position = (320,240)
            self.drawCameraView(i, picSize, position)
            i += 1

    def rotateCameraList(self):
        i = 0
        newCamerasList = [None] * len(self.cameras)
        while i < len(self.cameras):
            newCamerasList[len(self.cameras) - 1 - i] = self.cameras[i]
            i += 1
        self.cameras = newCamerasList
        print(self.cameras)

    def modelFrontCameraView(self, instanceIndex=0, size=(640,480), position=(0,0)):
        if len(self.cameras) >= 1:
            self.drawCameraView(instanceIndex, size, position)

    def drawCameraView(self, ind, picSize, position):
        if self.cameras[ind].query_image():
            image = self.cameras[ind].get_image()
            image = pygame.transform.scale(image, picSize)
            self.screen.blit(image, position)

    def modelBackCameraView(self):
        self._drawBackCameraPicture(160, 120, 240, 356)

    def modelAnimatedBackCameraView(self, inORout):
        step = 120
        if inORout:
            if self.backpx > self.backMaxpx:
                self.backpx = self.backpx - step
            if self.backpy > self.backMaxpy: 
                self.backpy = self.backpy - step
            if self.backx < self.backMaxx:
                self.backx = self.backx + step
            if self.backy < self.backMaxy: 
                self.backy = self.backy + step
        else:
            if self.backpx < self.backDefpx:
                self.backpx = self.backpx + step
            if self.backpy < self.backDefpy: 
                self.backpy = self.backpy + step
            if self.backx > self.backDefx:
                self.backx = self.backx - step
            if self.backy > self.backDefy: 
                self.backy = self.backy - step
        self._drawBackCameraPicture(self.backx, self.backy, self.backpx, self.backpy)

    def _drawBackCameraPicture(self, x, y, px, py):
        if len(self.cameras) >= 2:
            self.drawCameraView(1, (x,y), (px,py))

    def stopCameras(self):
        i = 0
        while i < len(self.cameras):
            self.cameras[i].stop()
            i += 1

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    #the order of instantiation matters!?
    testVideoDevices = ("/dev/video0", "/dev/video1", "/dev/video3")
    #testVideoDevices = ("/dev/cameraffront", "/dev/camerafback", "/dev/camerafront")
    #grid 4 cameras 320 x 240
    display = pygame.display.set_mode((640, 480), 0)
    cameras = cc_cameras(display, testVideoDevices)
    run = True
    while run:
        cameras.renderAllCameras((320, 240))
        pygame.display.flip()
        #pygame.display.update()
        pygame.time.wait(0)
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False
    cameras.stopCameras()
    pygame.quit()

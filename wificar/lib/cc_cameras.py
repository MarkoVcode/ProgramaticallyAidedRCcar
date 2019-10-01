import pygame
import cc_configuration

class cc_cameras:
    def __init__(self, screen):
        self.screen = screen
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
        if cc_configuration.isHardwareSupported():
            self.cam_list = cc_configuration.PI_CAMERAS
        else:
            self.cam_list = pygame.camera.list_cameras()
        if len(self.cam_list) >= 2:            
            self.camFront = pygame.camera.Camera(self.cam_list[0],(640,480))
            self.camBack  = pygame.camera.Camera(self.cam_list[1],(640,480))
            self.camFront.start()
            self.camBack.start()
        elif len(self.cam_list) == 1:
            self.camFront = pygame.camera.Camera(self.cam_list[0],(640,480))
            self.camBack = None      
            self.camFront.start()
        else:
            self.camFront = None
            self.camBack = None

    def modelFrontCameraView(self):
        if self.camFront:
            image = self.camFront.get_image()
            image = pygame.transform.scale(image,(640,480))
            self.screen.blit(image,(0,0))

    def modelBackCameraView(self):
        if self.camBack:
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
        image = self.camBack.get_image()
        image = pygame.transform.scale(image,(x,y))
        self.screen.blit(image,(px,py))

    def stopCameras(self):
        if self.camFront:
            self.camFront.stop()
        if self.camBack:            
            self.camBack.stop()

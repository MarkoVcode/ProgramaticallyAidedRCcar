import pygame
import cc_configuration

class cc_cameras:
    def __init__(self, screen):
        self.screen = screen
        if cc_configuration.isHardwareSupported():
            self.cam_list = cc_configuration.PI_CAMERAS
        else:
            self.cam_list = pygame.camera.list_cameras()
        if len(self.cam_list) >= 2:            
            self.camFront = pygame.camera.Camera(self.cam_list[0],(640,480))
            self.camBack  = pygame.camera.Camera(self.cam_list[1],(160,120))
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
            image = pygame.transform.scale(image,(720,480))
            self.screen.blit(image,(0,0))

    def modelBackCameraView(self):
        if self.camBack:
            image = self.camBack.get_image()
            image = pygame.transform.scale(image,(160,120))
            self.screen.blit(image,(240,356))

    def stopCameras(self):
        if self.camFront:
            self.camFront.stop()
        if self.camBack:            
            self.camBack.stop()

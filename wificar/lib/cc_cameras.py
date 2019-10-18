import pygame
import array

class cc_cameras:
    def __init__(self, screen):
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
        cam_list = pygame.camera.list_cameras()
        i = 0
        while i < len(cam_list): 
            try:
                cam = pygame.camera.Camera(cam_list[i],(640,480))
                cam.start()
                self.cameras.append(cam)
            except:
                print("cant initiate: " + cam_list[i])
            i += 1
        print("Discovered cameras: ")
        print(self.cameras)

    def rotateCameraList(self):
        i = 0
        newCamerasList = [None] * len(self.cameras)
        while i < len(self.cameras):
            newCamerasList[len(self.cameras) - 1 - i] = self.cameras[i]
            i += 1
        self.cameras = newCamerasList
        print(self.cameras)

    def modelFrontCameraView(self):
        if len(self.cameras) >= 1:
            image = self.cameras[0].get_image()
            image = pygame.transform.scale(image,(640,480))
            self.screen.blit(image,(0,0))

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
            image = self.cameras[1].get_image()
            image = pygame.transform.scale(image,(x,y))
            self.screen.blit(image,(px,py))

    def stopCameras(self):
        i = 0
        while i < len(self.cameras):
            self.cameras[i].stop()
            i += 1

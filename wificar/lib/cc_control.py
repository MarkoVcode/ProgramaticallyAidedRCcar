import pygame
import lib.cc_configuration as gameConfig

class cc_control:
    def __init__(self, udpClient):
        self.udpClient = udpClient
        self.pressedXcounter = 0
        self.throttlePressedCounter = 0
        self.direction = 0
        self.throttle = 0
        self.headlights = 0
        self.hudRendering = 1

    def direction_decrease(self, dirvalue):
        if dirvalue > gameConfig.DIR_MIN_POSITION:
            dirvalue = dirvalue-1
            self.udpClient.sendPWM('dir',dirvalue)
        return dirvalue
            
    def direction_increase(self, dirvalue):
        if dirvalue < gameConfig.DIR_MAX_POSITION:
            dirvalue = dirvalue+1
            self.udpClient.sendPWM('dir',dirvalue)
        return dirvalue

    def throttle_increase(self):
        self.udpClient.sendPWM('thr',1)

    def throttle_decrease(self):
        self.udpClient.sendPWM('thr',-1)
        
    def enable_headlights(self, headl):
        return_value = 0
        if headl > 0:
            self.udpClient.sendPWM('headl',0)
        else:
            self.udpClient.sendPWM('headl',1)
            return_value = 1
        return return_value

    def enable_hudRendering(self, hudr):
        return_value = 0
        if hudr == 0:
            return_value = 1
        elif hudr == 1:
            return_value = 2
        elif hudr == 2:
            return_value = 0      
        return return_value

    def processKeyboardEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direction = self.direction_decrease(self.direction)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direction = self.direction_increase(self.direction)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.throttlePressedCounter = pygame.time.get_ticks()
                if self.throttle < 1:
                   self.throttle_increase()
                   self.throttle = 1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.throttlePressedCounter = pygame.time.get_ticks()               
                if self.throttle > -1:
                   self.throttle_decrease()
                   self.throttle = -1                              
            if event.key == pygame.K_v:
                self.hudRendering = self.enable_hudRendering(self.hudRendering)             
            if event.key == pygame.K_h:
                self.udpClient.sendPWM('horn',1)                
            if event.key == pygame.K_h:
                self.udpClient.sendPWM('horn',1)
            if event.key == pygame.K_f:
                self.udpClient.sendPWM('headlblink',1)
            if event.key == pygame.K_g:
                self.headlights = self.enable_headlights(headlights)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                self.pressedXcounter = 0
            if event.key == pygame.K_h:
                self.udpClient.sendPWM('horn',0)
            if event.key == pygame.K_f:
                self.udpClient.sendPWM('headlblink',0)

    def processPressedKeys(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pressedXcounter = self.pressedXcounter+1
            if self.pressedXcounter > 1:
                self.pressedXcounter = 0
                self.direction = self.direction_decrease(self.direction)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pressedXcounter = self.pressedXcounter+1
            if self.pressedXcounter > 1:   
                self.pressedXcounter = 0
                self.direction = self.direction_increase(self.direction)
        if pygame.time.get_ticks() - gameConfig.KEEP_THROTTLE_PRESSED_MS > self.throttlePressedCounter:
            if self.throttle != 0:
                self.udpClient.sendPWM('thr',0)
                self.throttle = 0

    def getHudRendering(self):
        return self.hudRendering

    def getDirection(self):
        return self.direction

    def getThrottle(self):
        return self.throttle
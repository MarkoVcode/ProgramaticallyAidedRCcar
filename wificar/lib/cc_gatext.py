import pygame
from lib.cc_gtext import cc_gtext

COLOUR_WHITE = (255, 255, 255)
COLOUR_RED   = (252, 29, 25)

class cc_gatext:
    def __init__(self, screen):
        self.gtext = cc_gtext(screen)
        self.screen = screen
        self.delayCycle = 0
        self.currentFontSize = 16
        self.direction = True

    def pulseText(self, x, y, text):
        sizeMax = 16
        sizeMin = 15
        delay = 1

        if delay > self.delayCycle:
            self.delayCycle = self.delayCycle + 1
        else:
            self.delayCycle = 0
            if self.currentFontSize == sizeMax:
                self.direction = False
            elif self.currentFontSize == sizeMin:
                self.direction = True
            if self.direction:
                self.currentFontSize = self.currentFontSize + 1
            else:
                self.currentFontSize = self.currentFontSize - 1
        self.gtext.modelVarSizeText(320, 75, text, self.currentFontSize)

    def marqueeText(self, x, y, text):
        self.gtext.modelVarSizeText(320,75,text, 22)        
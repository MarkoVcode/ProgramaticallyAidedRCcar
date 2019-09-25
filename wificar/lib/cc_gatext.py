import pygame
from cc_gtext import cc_gtext

COLOUR_WHITE = (255, 255, 255)
COLOUR_RED   = (255, 0, 0)

class cc_gatext:
    def __init__(self, screen):
        self.gtext = cc_gtext(screen)
        self.screen = screen

    def pulseText(self, x, y, text):
        self.gtext.modelVarSizeText(320,75,text, 11)

    def marqueeText(self, x, y, text):
        self.gtext.modelVarSizeText(320,75,text, 22)        
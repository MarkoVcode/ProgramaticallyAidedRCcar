import pygame

COLOUR_WHITE = (255, 255, 255)
COLOUR_RED   = (255, 0, 0)

class cc_gtext:
    def __init__(self, screen):
        self.font = pygame.font.Font('fonts/Retron2000.ttf',11)
        self.warningFont = pygame.font.Font('fonts/Retron2000.ttf',17)
        self.screen = screen

    def modelText(self, x, y, text):
        TextSurf, TextRect = self.text_objects(text, self.font, COLOUR_WHITE)
        TextRect.center = (x,y)
        self.screen.blit(TextSurf, TextRect)

    def modelWarningText(self, x, y, text):
        TextSurf, TextRect = self.text_objects(text, self.warningFont, COLOUR_RED)
        TextRect.center = (x,y)
        self.screen.blit(TextSurf, TextRect)

    def modelVarSizeText(self, x, y, text, size):
        TextSurf, TextRect = self.text_objects(text, self.warningFont, COLOUR_RED)
        TextRect.center = (x,y)
        self.screen.blit(TextSurf, TextRect)        

    def text_objects(self, text, font, colour):
        textSurface = font.render(text, True, colour)
        return textSurface, textSurface.get_rect()
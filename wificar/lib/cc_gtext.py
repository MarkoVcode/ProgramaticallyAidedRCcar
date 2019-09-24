import pygame

COLOUR_WHITE=(255,255,255)

class cc_gtext:
    def __init__(self, screen):
       self.font = pygame.font.Font('fonts/PixelOperator.ttf',17)
       self.screen = screen

    def modelText(self, x, y, text):
        TextSurf, TextRect = self.text_objects(text, self.font)
        TextRect.center = (x,y)
        self.screen.blit(TextSurf, TextRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, COLOUR_WHITE)
        return textSurface, textSurface.get_rect()
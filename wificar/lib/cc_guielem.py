import pygame
from cc_gtext import cc_gtext

COLOUR_WHITE = (255, 255, 255)
COLOUR_CREAM = (225, 255, 200)
COLOUR_ORANGE = (252, 202, 3)
COLOUR_RED = (252, 29, 25)

HIGHLIGHT_HORIZON = (255, 255, 255, 20)

class cc_guielem:
    def __init__(self, screen):
       self.gtext = cc_gtext(screen)
       self.screen = screen
       self.currentVoltageValue=10

    def modelHorizonScale(self, x, y):
        screen_rect = self.screen.get_rect()
        see_through = pygame.Surface((300,300)).convert_alpha()
        see_through.fill(HIGHLIGHT_HORIZON)
        see_through_rect = see_through.get_rect(center=screen_rect.center)
        self.screen.blit(see_through, see_through_rect)
    #Vertical Lines
        point1 = 160, 120
        point2 = 160, 360
        pygame.draw.line(self.screen, COLOUR_WHITE, point1, point2)
        point3 = 480, 120
        point4 = 480, 360
        pygame.draw.line(self.screen, COLOUR_WHITE, point3, point4)

    #Number Lines Left
        point11 = 150, 120
        point12 = 160, 120
        pygame.draw.line(self.screen, COLOUR_WHITE, point11, point12)
        point7 = 150, 240
        point8 = 160, 240
        pygame.draw.line(self.screen, COLOUR_WHITE, point7, point8)
        point13 = 150, 360
        point14 = 160, 360
        pygame.draw.line(self.screen, COLOUR_WHITE, point13, point14)
        point23 = 155, 180
        point24 = 160, 180
        pygame.draw.line(self.screen, COLOUR_WHITE, point23, point24)
        point25 = 155, 300
        point26 = 160, 300
        pygame.draw.line(self.screen, COLOUR_WHITE, point25, point26)        

    #Number Lines Right
        point15 = 480, 120
        point16 = 490, 120
        pygame.draw.line(self.screen, COLOUR_WHITE, point15, point16)
        point9 = 480, 240
        point10 = 490, 240
        pygame.draw.line(self.screen, COLOUR_WHITE, point9, point10)
        point17 = 480, 360
        point18 = 490, 360
        pygame.draw.line(self.screen, COLOUR_WHITE, point17, point18)
        point19 = 480, 180
        point20 = 485, 180
        pygame.draw.line(self.screen, COLOUR_WHITE, point19, point20)
        point21 = 480, 300
        point22 = 485, 300
        pygame.draw.line(self.screen, COLOUR_WHITE, point21, point22)

    #Numbers Left
        self.gtext.modelText(136, 120, '180')
        self.gtext.modelText(140, 240, '0')
        self.gtext.modelText(136, 360, '180')

    #Numbers Right
        self.gtext.modelText(504, 120, '180')
        self.gtext.modelText(500, 240, '0')
        self.gtext.modelText(504, 360, '180')

        pygame.draw.circle(self.screen, (255,255,255), ((640/2),(480/2)), 2, 2)
    
    def modelHorizonLine(self, x, y, ax, ay, az):
        ax = round(ax * 12)
        ay = round(ay * 12)
        point5 = x, (y + ay) +ax
        point6 = x+280, (y - ay) +ax
        pygame.draw.line(self.screen, COLOUR_WHITE, point5, point6)

    def modelHorizonValues(self, x, y, ax, ay, az):
        self.gtext.modelText(x,y, 'x:'+str(ax))
        self.gtext.modelText(x,y + 13, 'y:'+str(ay))
        self.gtext.modelText(x,y + 26, 'z:'+str(az))

    def modelRoadOutline(self, x, y, dirValue):
        if dirValue == 0:
            point1 = 270+x, 0+y
            point2 = 170+x, 240+y
            pygame.draw.line(self.screen, COLOUR_CREAM, point1, point2, 1)
            point3 = 370+x, 0+y
            point4 = 470+x, 240+y
            pygame.draw.line(self.screen, COLOUR_CREAM, point3, point4, 1)
       # pygame.draw.circle(self.screen, (255,255,255), ((640/2),(480/2)), 2, 2)

    def modelWheelsState(self, x, y, dirValue, throttleValue):
        xoffset = -30
        yoffset = -200
        blue = 225, 255, 200
        point1 = 600+xoffset, 360+yoffset
        point2 = 600+xoffset, 430+yoffset
        pygame.draw.line(self.screen, blue, point1, point2, 3)
        point3 = 570+xoffset, 360+yoffset
        point4 = 630+xoffset, 360+yoffset
        pygame.draw.line(self.screen, blue, point3, point4, 3)
        point5 = 570+xoffset, 430+yoffset
        point6 = 630+xoffset, 430+yoffset
        pygame.draw.line(self.screen, blue, point5, point6, 3)
        pygame.draw.circle(self.screen, blue, (600+xoffset,360+yoffset), 5, 5)
        pygame.draw.circle(self.screen, blue, (600+xoffset,430+yoffset), 5, 5)
        #tyres front
        point9 = 570+dirValue+xoffset, 345+yoffset
        point10 = 570-dirValue+xoffset, 376+yoffset
        pygame.draw.line(self.screen, blue, point9, point10, 12)
        point11 = 630+dirValue+xoffset, 345+yoffset
        point12 = 630-dirValue+xoffset, 376+yoffset
        pygame.draw.line(self.screen, blue, point11, point12, 12)
        #tyres back
        point7 = 570+xoffset, 415+yoffset
        point8 = 570+xoffset, 446+yoffset
        pygame.draw.line(self.screen, blue, point7, point8, 12)
        point13 = 630+xoffset, 415+yoffset
        point14 = 630+xoffset, 446+yoffset
        pygame.draw.line(self.screen, blue, point13, point14, 12)
        if dirValue == 0:
            point15 = 583+xoffset, 360+yoffset
            point16 = 617+xoffset, 360+yoffset
            pygame.draw.line(self.screen, blue, point15, point16, 5)
        if throttleValue > 0:
            point17 = 583+xoffset, 350+yoffset
            point18 = 600+xoffset, 340+yoffset
            pygame.draw.line(self.screen, blue, point17, point18, 4)
            point21 = 600+xoffset, 340+yoffset
            point22 = 617+xoffset, 350+yoffset
            pygame.draw.line(self.screen, blue, point21, point22, 4)
            point23 = 583+xoffset, 340+yoffset
            point24 = 600+xoffset, 330+yoffset
            pygame.draw.line(self.screen, blue, point23, point24, 4)
            point25 = 600+xoffset, 330+yoffset
            point26 = 617+xoffset, 340+yoffset
            pygame.draw.line(self.screen, blue, point25, point26, 4)
        if throttleValue < 0:
            point27 = 583+xoffset, 440+yoffset
            point28 = 600+xoffset, 450+yoffset
            pygame.draw.line(self.screen, blue, point27, point28, 4)
            point29 = 600+xoffset, 450+yoffset
            point30 = 617+xoffset, 440+yoffset
            pygame.draw.line(self.screen, blue, point29, point30, 4)
            point31 = 583+xoffset, 450+yoffset
            point32 = 600+xoffset, 460+yoffset
            pygame.draw.line(self.screen, blue, point31, point32, 4)
            point33 = 600+xoffset, 460+yoffset
            point34 = 617+xoffset, 450+yoffset
            pygame.draw.line(self.screen, blue, point33, point34, 4) 

    def modelPowerMetrics(self, x, y, batteryVolt, rpiVoltage, rpiCurr):      
        self.gtext.modelText(x, y, 'Bat: ' + str(batteryVolt) + 'V')
        self.gtext.modelText(x, y + 13, 'Bat cell: ' + str(round((batteryVolt/2),1)) + 'V')
        self.gtext.modelText(x, y + 26, 'PI: ' + str(rpiVoltage) + 'V')
        self.gtext.modelText(x, y + 39, 'PI: ' + str(rpiCurr) + 'A')      

    def modelSystemMetrics(self, x, y, rpiStabTemp):            
        self.gtext.modelText(x, y + 52, 'PI core: ' + str(rpiStabTemp) + 'C') 

    def modelBatteryLevel(self, x, y, l, batteryVolt, minVolt, maxVolt, varnVolt, critVolt):
        step = 1
        barColour = COLOUR_CREAM
        if batteryVolt <= critVolt:
            barColour = COLOUR_RED
        elif batteryVolt <= varnVolt:
            barColour = COLOUR_ORANGE
        if batteryVolt > minVolt:
            lv = 0
            if batteryVolt <= maxVolt:  
                unit = l/(maxVolt - minVolt)
                lv = round((batteryVolt-minVolt) * unit)
                if self.currentVoltageValue < lv:
                    self.currentVoltageValue = self.currentVoltageValue + step
                if self.currentVoltageValue > lv:
                    self.currentVoltageValue = self.currentVoltageValue - step
            else:
                self.currentVoltageValue = l
            point1 = x+10, y+5
            point2 = x+self.currentVoltageValue, y+5
            pygame.draw.line(self.screen, barColour, point1, point2, 6)
        
        point3 = x+10, y+11
        point4 = x+l, y+11
        pygame.draw.line(self.screen, COLOUR_CREAM, point3, point4, 1)
        point5 = x+10, y
        point6 = x+l, y
        pygame.draw.line(self.screen, COLOUR_CREAM, point5, point6, 1)

        self.gtext.modelText(x,y+6, '0')        
        self.gtext.modelText(x+l+20,y+6, '100%')
    

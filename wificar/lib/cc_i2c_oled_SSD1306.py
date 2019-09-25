import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# define a class
class cc_i2c_oled_SSD1306:
    def __init__(self):
        # 128x32 display with hardware I2C:
        #disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        # 128x64 display with hardware I2C:
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        # Note you can change the I2C address by passing an i2c_address parameter like:
        # disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

        # Alternatively you can specify an explicit I2C bus number, for example
        # with the 128x32 display you would use:
        # disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

        # Initialize library.
        self.disp.begin()

    def writeText(self, text):
        self.render(text)

    def render(self, text):
        # Clear display.
        self.disp.clear()
        self.disp.display()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        width = self.disp.width
        height = self.disp.height
        image = Image.new('1', (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        font = ImageFont.load_default()
        #font = ImageFont.truetype('Minecraftia.ttf', 8)
        textElems = text.split(";",)
        lineSpace = 0
        for i in textElems:
            draw.text((1, 15 + lineSpace), i, font=font, fill=255)
            lineSpace = lineSpace + 10
        self.disp.image(image)
        self.disp.display()
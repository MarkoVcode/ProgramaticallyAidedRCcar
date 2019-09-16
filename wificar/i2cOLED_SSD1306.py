import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# define a class
class OLEDdisplay:
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

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = 2
        shape_width = 20
        top = padding
        bottom = height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = padding
        # Draw an ellipse.
        #draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
        #x += shape_width+padding
        # Draw a rectangle.
        #draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
        #x += shape_width+padding
        # Draw a triangle.
        #draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
        #x += shape_width+padding
        # Draw an X.
        #draw.line((x, bottom, x+shape_width, top), fill=255)
        #draw.line((x, top, x+shape_width, bottom), fill=255)
        #x += shape_width+padding
        x = 5
        #font = ImageFont.load_default()
        #font = ImageFont.truetype('Minecraftia.ttf', 8)
        #font = ImageFont.truetype('fonts/VCR_OSD_MONO_1.001.ttf', 10)
        font = ImageFont.truetype('fonts/PixelOperator.ttf', 14)

        draw.text((x, top),    text,  font=font, fill=255)
        #draw.text((x, top+20), 'World!', font=font, fill=255)

        self.disp.image(image)
        self.disp.display()
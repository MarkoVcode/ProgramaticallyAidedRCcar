import time
import logging
import smbus

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class cc_i2c_io_PCF8574:
    def __init__(self):
        print("PCF8574")

    def init(self):
        print("PCF8574 init")


       #https://www.raspberrypi.org/forums/viewtopic.php?t=176643
       #https://github.com/flyte/pcf8574/blob/develop/pcf8574/__init__.py
       #pibits.net/code/raspberry-pi-pcf8574-example.php
        LED1 = 0x01
        LED2 = 0x02
        LED3 = 0x04
        LED4 = 0x08
        LED5 = 0x10
        LED6 = 0x20
        LED7 = 0x40
        LED8 = 0x80
        bus = smbus.SMBus(1)
        
        while True:
            bus.write_byte(0x20, LED1)
            #bus.w
            time.sleep(0.5)
            bus.write_byte(0x20, LED2)
            time.sleep(0.5)
            bus.write_byte(0x20, LED3)
            time.sleep(0.5)
            bus.write_byte(0x20, LED4)
            time.sleep(0.5)

if __name__ == '__main__':
    io = cc_i2c_io_PCF8574()

import socket
import sys
import logging
import json
import cc_configuration

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

# throttle neutral 350 max 370 min 330
# dir neutral 340 max 380 min 300

#mesages from keyboard
message = 'i2c:pwm:dir:0'
#message = 'i2c:pwm:dir:-5'
#message = 'i2c:pwm:dir:5'
#message = 'i2c:pwm:thr:0'
#message = 'i2c:pwm:thr:1'
#message = 'gpio:pin:ls1:0'  # lights short (including back)
#message = 'gpio:pin:ll2:0'  # lights long (both lights)
#message = 'gpio:pin:indl:0'   #  indicator left  not exposed on UI
#message = 'gpio:pin:indr:0'    # indicator right not exposed on UI
#message = 'gpio:pin:horn:0'    # audio warning
#message = 'gpio:pin:horn:1'
#message from the web app
#message = 'gpio:pin:engaged:0' # engaged warning LED
#message = 'i2c:oled:msg:192.168.0.33;q2;engaged'
#message = 'read:i2c'

#UDP_SERVER_ADDRESS = 'localhost'
#UDP_SERVER_PORT = 10000

UDP_MESSAGE_PREFIX_I2C_PWM = 'i2c:pwm:'
UDP_MESSAGE_PREFIX_GPIO_PIN = 'gpio:pin:'
UDP_MESSAGE_PREFIX_I2C_OLED = 'i2c:oled:'
UDP_MESSAGE_PREFIX_SENSOR_READ = 'read:'

# define a class
class cc_udpclient:
    def __init__(self):
       self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       self.server_address = (cc_configuration.UDP_SERVER_ADDRESS, cc_configuration.UDP_SERVER_PORT)
       self.connected = True
	
    def sendPWM(self, channel, value):
        message = UDP_MESSAGE_PREFIX_I2C_PWM + str(channel) + ':' + str(value)
        self.dispatch(message)

    def sendGPIOPIN(self, pin, value):
        message = UDP_MESSAGE_PREFIX_GPIO_PIN + str(pin) + ':' + str(value)
        self.dispatch(message)
    
    def sendLCD(self, type, value):
        message = UDP_MESSAGE_PREFIX_I2C_OLED + str(type) + ':' + str(value)
        self.dispatch(message)

    def fetchSensors(self, sensor):
        message = UDP_MESSAGE_PREFIX_SENSOR_READ + str(sensor)
        responseString = self.dispatch(message)
        if responseString:
            jsonAcceptableString = responseString.replace("'", "\"")
            return json.loads(jsonAcceptableString)
        else:
            return {}

    def dispatch(self, message):
        data = None
        try:
            self.sock.settimeout(0.1)
            sent = self.sock.sendto(message, self.server_address)
            data, server = self.sock.recvfrom(4096)
            self.connected = True
        except:
            self.connected = False
        return data
    
    def isConnectionAlive(self):
        return self.connected

if __name__ == '__main__':
    p = cc_udpclient()
   # p.dispatch(message)
    print(__name__)
    sensors = p.fetchSensors("ALL")
    print(sensors)
   # p.sendGPIOPIN('ls1',0)
   # p.sendPWM('dir', 2)
   # p.sendLCD('msg','my message')

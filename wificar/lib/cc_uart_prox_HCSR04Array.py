import logging
from time import sleep
import serial
import cc_configuration as gameConfig

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

ERROR_READINGS = "err"
# sudo usermod -a -G dialout pi

class cc_uart_prox_HCSR04Array:
    def __init__(self):
        self.ser = None
        self.values = None
        self.lastRead = None

    def _init_serial(self):
        if not self.hasConnection():
            try:
                self.ser = serial.Serial(gameConfig.PROXYMITY_SENSOR_UART, gameConfig.PROXYMITY_SENSOR_UART_SPEED) # Establish the connection on a specific port
                return True
            except Exception as e:
                self.ser = None
                logging.debug('Serial NOT connected! error: {0}'.format(e))
                return False
        else:
            return True

    def getData(self):
        return self._fetch_reading()

    def _fetch_reading(self):
        line = ERROR_READINGS
        self._init_serial()
        try:
            self.ser.write("n")
            line = self.ser.readline() # Read the newest output from the Arduino
        except Exception as e:
            self.ser = None
            logging.debug('Can not read serial: ' + str(gameConfig.PROXYMITY_SENSOR_UART) + ', error: {0}'.format(e))
        return line

    def hasConnection(self):
        if self.ser:
            return True
        else:
            return False

if __name__ == '__main__':
    sonArr = cc_uart_prox_HCSR04Array()
    print(sonArr.getData())

#dziala
#    import serial, time
#    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
#    time.sleep(1) #give the connection a second to settle
#    arduino.write("Hello from Python!")
#    while True:
#        arduino.write("n")
#        data = arduino.readline()
#        if data:
#            print data.rstrip('\n') #strip out the new lines for now
            # (better to do .read() in the long run for this reason
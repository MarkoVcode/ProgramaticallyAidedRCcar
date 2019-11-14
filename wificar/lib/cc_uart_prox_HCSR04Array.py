import logging
from time import sleep
import serial
import cc_configuration as gameConfig
import json
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

ERROR_READINGS = "{\"Z\":0}"

# sudo usermod -a -G dialout pi

class cc_uart_prox_HCSR04Array:
    def __init__(self):
        self.ser = None
        self.values = None
        self.lastRead = None
        self.errorsCounter = gameConfig.MUTE_REPETITIVE_ERRORS_AFTER_OCURRENCES

    def _init_serial(self):
        if not self.hasConnection():
            try:
                self.ser = serial.Serial(gameConfig.PROXYMITY_SENSOR_UART, gameConfig.PROXYMITY_SENSOR_UART_SPEED) # Establish the connection on a specific port
                self.errorCounterReset()
                return True
            except Exception as e:
                self.ser = None
                if self.errorCounter():
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
            self.errorCounterReset()
        except Exception as e:
            self.ser = None
            if self.errorCounter():
                logging.debug('Can not read serial: ' + str(gameConfig.PROXYMITY_SENSOR_UART) + ', error: {0}'.format(e))
        return json.loads(line)
        #, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    def hasConnection(self):
        if self.ser:
            return True
        else:
            return False

    def errorCounter(self):
        if self.errorsCounter > 0:
            self.errorsCounter = self.errorsCounter - 1
            return True
        return False

    def errorCounterReset(self):
        self.errorsCounter = gameConfig.MUTE_REPETITIVE_ERRORS_AFTER_OCURRENCES

if __name__ == '__main__':
    sonArr = cc_uart_prox_HCSR04Array()
    data = sonArr.getData()
    datax = {}
    for key in data:
        datax[str(key)] = data[key]
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    x['proxi'] = {'data': datax}
    print(x)
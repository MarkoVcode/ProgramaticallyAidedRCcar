from time import sleep
import serial
import lib.cc_configuration as gameConfig

class cc_uart_prox_ARRAY:
    def __init__(self):
        #cover exception
        self.ser = None
        self.values = None
        self.lastRead = None

    def _init_serial(self):
        if not self.hasConnection():
            try:
                self.ser = serial.Serial(gameConfig.PROXYMITY_SENSOR_UART, gameConfig.PROXYMITY_SENSOR_UART_SPEED) # Establish the connection on a specific port
                return True
            except:
                self.ser = None
                return False
        else:
            return True

    def _fetch_reading(self):
        self._init_serial()
        try:
            line = self.ser.readline() # Read the newest output from the Arduino
            # process readings here
        except:
            self.ser = None

        #counter = 32 # Below 32 everything in ASCII is gibberish
        #while True:
     #counter +=1
     #ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
            line = self.ser.readline() # Read the newest output from the Arduino
        #    sleep(.1) # Delay for one tenth of a second
     #if counter == 255:
      #  counter = 32

    def hasConnection(self):
        if self.ser:
            return True
        else:
            return False

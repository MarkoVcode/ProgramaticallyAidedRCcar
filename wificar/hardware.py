import logging
import random
import string
#import Adafruit_PCA9685

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

#Hardware init

def interactionID(stringLength=5):
    letters = string.ascii_lowercase
    return '['+''.join(random.choice(letters) for i in range(stringLength)) + ']'

READ_SENSORS_CYCLE_SKIP = 4000000

# define a class
class HardwareStrategy:
    def __init__(self):
       self.read_sensor_cycle_counter = 0
       self.sensors = {}
       self.sensorCycle = [1, 0, 0]
       print "Hardware Init"
       
       #pwm = Adafruit_PCA9685.PCA9685()
       #pwm.set_pwm_freq(60)

	
    def executeIOInteraction(self, intId, instruction):
        instElems = instruction.split(":",)
        if instElems[0] == "i2c":
            #print "I2C message!"
            if instElems[1] == "pwm":
                #print "EXECUTE Adafruit_PCA9685.PCA9685"
                #convert to PWM values here
                #pwm.set_pwm(3, 0, x_change)
                #pwm.set_pwm(2, 0, y_change)
                logging.debug(intId + ' EXECUTE I2C-PCA9685 Channel: ' + str(instElems[2]) 
                              + ' Value: ' + str(instElems[3]))
        elif instElems[0] == "gpio":
            #print "GPIO message!"
            if instElems[1] == "pin":
                #print "EXECUTE GPIO PIN CHANGE"
                #convert to pin number here
                #gpo operation
                logging.debug(intId + ' EXECUTE GPIO-PIN Number: ' + str(instElems[2]) 
                              + ' Value: ' + str(instElems[3]))
        else:
            print "Message Unrecognized - IGNORE"

    def fetchSensors(self, selectedSensor):
        if selectedSensor == 'ALL':
            return self.sensors
        else:
            return self.sensors[selectedSensor]

    def readAllSensorsCycle(self):
        if self.read_sensor_cycle_counter >= READ_SENSORS_CYCLE_SKIP :
            print "Reading sensor from cycle"
            self.cycleSensorsRead()
            self.read_sensor_cycle_counter = 0
        else:
            self.read_sensor_cycle_counter = self.read_sensor_cycle_counter +1

    def cycleSensorsRead(self):
        if self.sensorCycle[0] == 1:
            self.readSensorsGPS()
            self.sensorCycle[0] = 0
            self.sensorCycle[1] = 1
            return
        elif self.sensorCycle[1] == 1:
            self.readSensorsI2C()
            self.sensorCycle[1] = 0
            self.sensorCycle[2] = 1
            return            
        elif self.sensorCycle[2] == 1:                
            self.readSensors1W()
            self.sensorCycle[2] = 0
            self.sensorCycle[0] = 1
            return              

    def readSensorsGPS(self):
        self.sensors['gps'] = {"qqq":"dds"}
        print "Reading GPS"

    def readSensorsI2C(self):
        self.sensors['i2c'] = ""
        print "Reading I2C"

    def readSensors1W(self):
        self.sensors['1w'] = ""
        print "Reading 1W"
import logging
import random
import string
import gameConfig
import os
import time

if gameConfig.isHardwareSupported():
    import Adafruit_PCA9685
    
    from mpu6050 import mpu6050

    from i2cOLED_SSD1306 import OLEDdisplay


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

#Hardware init

READ_SENSORS_CYCLE_SKIP = 4000000

# define a class
class HardwareStrategy:
    def __init__(self):
       self.read_sensor_cycle_timer = 0
       self.sensors = {}
       self.sensorCycle = [1, 0, 0]
       print "Hardware Init"
       if gameConfig.isHardwareSupported():
           self.pwm = Adafruit_PCA9685.PCA9685()
           self.pwm.set_pwm_freq(60)
           #init oled here
           self.oled = OLEDdisplay()
           self.accelerometer = mpu6050(0x68)

    def interactionID(self, stringLength=5):
        letters = string.ascii_lowercase
        return '['+''.join(random.choice(letters) for i in range(stringLength)) + ']'

    def executeIOInteraction(self, intId, instruction):
        instElems = instruction.split(":",)
        if instElems[0] == "i2c":
            #print "I2C message!"
            if instElems[1] == "pwm":
                #print "EXECUTE Adafruit_PCA9685.PCA9685"
                if instElems[2] == 'dir':
                    if gameConfig.isHardwareSupported():
                        self.pwm.set_pwm(gameConfig.CAR_STEER_PWM_CHANNEL, 0, self.calculateServoPWMValue(instElems[3]))
                    logging.debug(intId + ' EXECUTE I2C-PCA9685 STEER: ' + str(gameConfig.CAR_STEER_PWM_CHANNEL) 
                              + ' Value: ' + str(self.calculateServoPWMValue(instElems[3])))
                if instElems[2] == 'thr':
                    if gameConfig.isHardwareSupported():
                        self.pwm.set_pwm(gameConfig.CAR_THROTTLE_PWM_CHANNEL, 0, self.calculateThrottlePWMValue(instElems[3]))
                    logging.debug(intId + ' EXECUTE I2C-PCA9685 THROTTLE: ' + str(gameConfig.CAR_STEER_PWM_CHANNEL) 
                              + ' Value: ' + str(self.calculateServoPWMValue(instElems[3])))
                logging.debug(intId + ' EXECUTE I2C-PCA9685 Channel: ' + str(instElems[2]) 
                              + ' Value: ' + str(instElems[3]))
            if instElems[1] == "oled":
                if gameConfig.isHardwareSupported():
                    self.oled.writeText(instElems[2])
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

    def calculateServoPWMValue(self, requestedValue):
        if requestedValue == '0':
            return 340
        elif requestedValue == '1':
            return 350
        elif requestedValue == '2':
            return 360
        elif requestedValue == '3':
            return 370
        elif requestedValue == '4':
            return 380
        elif requestedValue == '5':
            return 390
        elif requestedValue == '-1':
            return 330
        elif requestedValue == '-2':
            return 320
        elif requestedValue == '-3':
            return 310
        elif requestedValue == '-4':
            return 300
        elif requestedValue == '-5':
            return 290
        else:
            return 340

    def calculateThrottlePWMValue(self, requestedValue):
        if requestedValue == '0':
            return 350
        elif requestedValue == '1':
            return 370
        elif requestedValue == '-1':
            return 330
        else:
            return 350

    def fetchSensors(self, selectedSensor):
        if selectedSensor == 'ALL':
            return self.sensors
        else:
            return self.sensors[selectedSensor]

    def readAllSensorsCycle(self):
        milli_sec = int(round(time.time() * 1000))
        if milli_sec - gameConfig.UPDATE_SENSORS_EVERY_MS > self.read_sensor_cycle_timer:
            self.cycleSensorsRead()
            self.read_sensor_cycle_timer = milli_sec

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

    def readSensorsI2C(self):
        if gameConfig.isHardwareSupported():
            accelerometer_data = self.accelerometer.get_accel_data()
            self.sensors['accel'] = accelerometer_data

    def readSensors1W(self):
        self.sensors['1w'] = ""
import logging
import random
import string
import os
import time
import subprocess
import cc_configuration
from cc_sensor_filters import *

if cc_configuration.isHardwareSupported():
    import Adafruit_PCA9685
    #from mpu6050 import mpu6050
    from cc_i2c_accel_MPU6050 import cc_i2c_accel_MPU6050
    from cc_i2c_oled_SSD1306 import cc_i2c_oled_SSD1306
    from cc_i2c_adc_ADS1115 import cc_i2c_adc_ADS1115

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

#Hardware init

#READ_SENSORS_CYCLE_SKIP = 4000000

# define a class
class cc_sensors:
    def __init__(self):
       self.read_sensor_cycle_timer = 0
       self.sensors = {}
       self.sensorCycle = [1, 0, 0]
       self.kf = EWMAFilter()
       self.filtersSMA = {}
       self.filtersEWMA = {}
       print "Hardware Init"
       if cc_configuration.isHardwareSupported():
           self.pwm = Adafruit_PCA9685.PCA9685()
           self.pwm.set_pwm_freq(60)
           #init oled here
           self.oled = cc_i2c_oled_SSD1306()
           self.accelerometer = cc_i2c_accel_MPU6050()
           self.accelerometer.initAccel(0x68)
           #self.accelerometer = mpu6050(0x68)
           self.power = cc_i2c_adc_ADS1115()

    def interactionID(self, stringLength=5):
        letters = string.ascii_lowercase
        return '['+''.join(random.choice(letters) for i in range(stringLength)) + ']'

    def executeIOInteraction(self, intId, instruction):
        instElems = instruction.split(":",)
        if instElems[0] == "i2c":
            if instElems[1] == "pwm":
                if instElems[2] == 'dir':
                    if cc_configuration.isHardwareSupported():
                        self.pwm.set_pwm(cc_configuration.CAR_STEER_PWM_CHANNEL, 0, self.calculateServoPWMValue(instElems[3]))
                    logging.debug(intId + ' EXECUTE I2C-PCA9685 STEER: ' + str(cc_configuration.CAR_STEER_PWM_CHANNEL) 
                              + ' Value: ' + str(self.calculateServoPWMValue(instElems[3])))
                if instElems[2] == 'thr':
                    if cc_configuration.isHardwareSupported():
                        self.pwm.set_pwm(cc_configuration.CAR_THROTTLE_PWM_CHANNEL, 0, self.calculateThrottlePWMValue(instElems[3]))
                    logging.debug(intId + ' EXECUTE I2C-PCA9685 THROTTLE: ' + str(cc_configuration.CAR_STEER_PWM_CHANNEL) 
                              + ' Value: ' + str(self.calculateServoPWMValue(instElems[3])))
                logging.debug(intId + ' EXECUTE I2C-PCA9685 Channel: ' + str(instElems[2]) 
                              + ' Value: ' + str(instElems[3]))
            if instElems[1] == "oled":
                if cc_configuration.isHardwareSupported():
                    self.oled.writeText(instElems[2])
        elif instElems[0] == "gpio":
            if instElems[1] == "pin":
                #print "EXECUTE GPIO PIN CHANGE"
                #convert to pin number here
                #gpo operation
                logging.debug(intId + ' EXECUTE GPIO-PIN Number: ' + str(instElems[2]) 
                              + ' Value: ' + str(instElems[3]))
        else:
            print "Message Unrecognized - IGNORE"

    def calculateServoPWMValue(self, requestedValue):
        #it is prepared to model non-linear progression here
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
        if milli_sec - cc_configuration.UPDATE_SENSORS_EVERY_MS > self.read_sensor_cycle_timer:
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
            self.readSystemMetrix()
            self.sensorCycle[1] = 0
            self.sensorCycle[2] = 1
            return
        elif self.sensorCycle[2] == 1:
            self.readSensors1W()
            self.readSensorsProximity()
            self.sensorCycle[2] = 0
            self.sensorCycle[0] = 1
            return

    def readSensorsGPS(self):
        if cc_configuration.isHardwareSupported():
            self.sensors['gps'] = {"qqq":"dds"}
        else:
            self.sensors['gps'] = {"qqq":"dds"}

    def readSensorsI2C(self):
        if cc_configuration.isHardwareSupported():
            accelerometer_data = self.accelerometer.getData()
            power_data = self.power.get_power_data()
            #print(power_data)
            self.sensors['accel'] = accelerometer_data
            self.sensors['power'] = power_data
            self.sensors['accel_flt'] = self.filterAccelerometerReading(accelerometer_data)
            self.sensors['power_flt'] = self.filterPowerReading(power_data)
        else:
            self.sensors['accel'] = {'x':-1.7860744384765623,'y':-9.016563452148437,'z':2.205059729003906}
            self.sensors['power'] = {"battery_volt":7.5, "pi_volt":5.1, "pi_current": 3.2}
            self.sensors['accel_flt'] = self.filterAccelerometerReading({'x':-1.7860744384765623,'y':-9.016563452148437,'z':2.205059729003906})
            self.sensors['power_flt'] = self.filterPowerReading({"battery_volt":7.5, "pi_volt":5.1, "pi_current": 3.2})

    def filterAccelerometerReading(self, values):
        return self._filterSMAValuesInDict(values)

    def filterPowerReading(self, values):
        return self._filterSMAValuesInDict(values)
    
    def filterSystemReading(self, values):
        return self._filterEWMAValuesInDict(values)

    def _filterSMAValuesInDict(self, values):
        filteredValues = {}
        for key in values:
            if key not in self.filtersSMA:
                self.filtersSMA[key] = SMAFilter()
                valuex = self.filtersSMA[key].filter(values[key])
            else:
                valuex = self.filtersSMA[key].filter(values[key])
            filteredValues[key] = valuex
        return filteredValues

    def _filterEWMAValuesInDict(self, values):
        filteredValues = {}
        for key in values:
            if key not in self.filtersEWMA:
                self.filtersEWMA[key] = EWMAFilter()
                valuex = self.filtersEWMA[key].filter(values[key])
            else:
                valuex = self.filtersEWMA[key].filter(values[key])
            filteredValues[key] = valuex
        return filteredValues        

    def readSystemMetrix(self):
        if cc_configuration.isHardwareSupported():
            #cmd =["vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'"]
            cmd =["vcgencmd measure_temp | egrep -o '[0-9]*\.' | egrep -o '[0-9]*'"]
            address = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (out, err) = address.communicate()
            system_data = {"core_temp":int(out)}
            self.sensors['system'] = system_data
            self.sensors['system_flt'] = self.filterSystemReading(system_data)
        else:
            self.sensors['system'] = {"core_temp":33.05555555555}
            self.sensors['system_flt'] = self.filterSystemReading({"core_temp":33.05555555555})

    def readSensors1W(self):
        if cc_configuration.isHardwareSupported():
            self.sensors['1w'] = ""
        else:
            self.sensors['1w'] = {'sensor1': 23}
        
    def readSensorsProximity(self):
        if cc_configuration.isHardwareSupported():
            self.sensors['proxi'] = {'A': 23}
        else:
            self.sensors['proxi'] = {'A': 23}
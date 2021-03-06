import time
import logging
import Adafruit_ADS1x15
import cc_configuration as gameConfig

ADC_RESOLUTION = 65536
BATTERY_VOLTAGE_RANGE = 4.096 * 2  #gain 1
PI_VOLTAGE_RANGE = 6.144 * 2       #gain 2/3
PI_CURRENT_RANGE = 0.512 * 2    #gain 8
BATTERY_VOLTAGE_DIVIDER_RATIO = 2.54777070063694
PI_VOLTAGE_CURRENT_MULTIPLYIER = -10.5

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = [1, 2/3, 8, 1]

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

DEFAULT_ADC_READING = (6.4, 5.0, 3.0, 0.0)

class cc_i2c_adc_ADS1115:
    def __init__(self):
       self.adc = None
       self.calcVal = None
       self.errorsCounter = gameConfig.MUTE_REPETITIVE_ERRORS_AFTER_OCURRENCES
       self.init()

    def init(self):
        success = False
        try:
            self.adc = Adafruit_ADS1x15.ADS1115()
            success = True
            self.errorCounterReset()
        except Exception as e:
            if self.errorCounter():
                logging.debug('ADS1115 - not present: {0}'.format(e))
        return success       

    def getPowerData(self):
        vals = None
        self.getValues()
        if self.calcVal == None:
            self.getValues()
        if self.calcVal is not None:
            vals = self.calcVal
        else:
            vals = DEFAULT_ADC_READING
        return {"battery_volt": vals[0], "pi_volt": vals[1], "pi_current": vals[2]}
        
    
    def getValues(self):
        if self.adc is None:
            if self.init():
                self._getValues()
            else:
                self.calcVal = DEFAULT_ADC_READING
        else:
            self._getValues()

    def errorCounter(self):
        if self.errorsCounter > 0:
            self.errorsCounter = self.errorsCounter - 1
            return True
        return False

    def errorCounterReset(self):
        self.errorsCounter = gameConfig.MUTE_REPETITIVE_ERRORS_AFTER_OCURRENCES

    def _getValues(self):
        values = [0]*4
        valuesCalculated = [0]*4
        for i in range(4):
            try:
                values[i] = self.adc.read_adc(i, gain=GAIN[i])
                if i == 0:
                    valuesCalculated[i] = round((((BATTERY_VOLTAGE_RANGE / ADC_RESOLUTION) * values[i]) * BATTERY_VOLTAGE_DIVIDER_RATIO),1)
                if i == 1:
                    valuesCalculated[i] = round(((PI_VOLTAGE_RANGE / ADC_RESOLUTION) * values[i]),1)
                if i == 2:
                    valuesCalculated[i] = round((((PI_CURRENT_RANGE / ADC_RESOLUTION) * values[i]) * PI_VOLTAGE_CURRENT_MULTIPLYIER),1)
                if i == 3:
                    valuesCalculated[i] = values[i]
                self.calcVal = valuesCalculated
                self.errorCounterReset()
            except Exception as e:
                if self.errorCounter():
                    logging.debug('ADC - connection issue: {0}'.format(e))

if __name__ == '__main__':
    adc = cc_i2c_adc_ADS1115()
    print(adc.getPowerData())


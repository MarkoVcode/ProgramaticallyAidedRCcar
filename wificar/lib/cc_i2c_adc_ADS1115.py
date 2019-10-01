import time
import Adafruit_ADS1x15

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

class cc_i2c_adc_ADS1115:
    def __init__(self):
       self.adc = Adafruit_ADS1x15.ADS1115()
       self.calcVal = None
    def get_power_data(self):
        self.getValues()
        if self.calcVal == None:
            self.getValues()
        return {"battery_volt": self.calcVal[0], "pi_volt": self.calcVal[1], "pi_current": self.calcVal[2]}

    def getValues(self):
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
            except:
                print("ADC - connection issue")


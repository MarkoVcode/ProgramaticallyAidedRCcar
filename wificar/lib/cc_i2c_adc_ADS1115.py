import time
import Adafruit_ADS1x15

ADC_RESOLUTION = 65536
BATTERY_VOLTAGE_RANGE = 4.096 * 2  #gain 1
PI_VOLTAGE_RANGE = 6.144 * 2       #gain 2/3
PI_CURRENT_RANGE = 0.512 * 2    #gain 8
BATTERY_VOLTAGE_DIVIDER_RATIO = 2.54777070063694

val = ((BATTERY_VOLTAGE_RANGE / ADC_RESOLUTION) * 28280 ) * BATTERY_VOLTAGE_DIVIDER_RATIO

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

    def get_power_data(self):
        values = self.getValues()
        print("sss")
        print(values)
        return {"battery_volt": round(values[0],1), "pi_volt": round(values[1],1), "pi_current": round(values[2],1)}
    
    def getValues(self):
        values = [0]*4
        valuesCalculated = [0]*4
        for i in range(4):
            values[i] = self.adc.read_adc(i, gain=GAIN[i])
            if i == 0:
                valuesCalculated[i] = round((((BATTERY_VOLTAGE_RANGE / ADC_RESOLUTION) * values[i] ) * BATTERY_VOLTAGE_DIVIDER_RATIO),1)
            if i == 1:
                valuesCalculated[i] = (PI_VOLTAGE_RANGE / ADC_RESOLUTION) * values[i]
            if i == 2:
                valuesCalculated[i] = (PI_CURRENT_RANGE / ADC_RESOLUTION) * values[i]   #here convert to Amps
            else:
                valuesCalculated[i] = values[i]
        return valuesCalculated

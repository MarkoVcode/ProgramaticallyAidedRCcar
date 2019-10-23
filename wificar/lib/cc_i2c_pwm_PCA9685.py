import time
import logging
import Adafruit_PCA9685

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class cc_i2c_pwm_PCA9685:
    def __init__(self):
        self.pwm = None
        self.init()
 
    def init(self):
        success = False
        try:
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.pwm.set_pwm_freq(60)
            success = True
        except:
            logging.debug('PCA9685 - not present')
        return success

    def set_pwm(self, channel, something, pwmvalue):
        if self.pwm is None:
            if self.init():
                self._set_pwm(channel, something, pwmvalue)
        else:
            self._set_pwm(channel, something, pwmvalue)

    def _set_pwm(self, channel, something, pwmvalue):
        try:
            self.pwm.set_pwm(channel, something, pwmvalue)
        except:
            logging.debug('PCA9685 - not present')
            self.pwm = None

if __name__ == '__main__':
    pwm = cc_i2c_pwm_PCA9685()
    pwm.set_pwm(5,0, 300)
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=3)

pwm.set_pwm_freq(60)
pwm.set_pwm(3, 0, 700)
pwm.set_pwm(2, 0, 100)
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

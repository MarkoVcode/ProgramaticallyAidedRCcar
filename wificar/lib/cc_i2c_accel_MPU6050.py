
import cc_configuration
import logging
from mpu6050 import mpu6050

DEFAULT_ACCEL_READING = {'x': 0, 'y': 0, 'z': 0}

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class cc_i2c_accel_MPU6050:
    def __init__(self):
        self.accelerometer = None
        self.offsetX = None
        self.offsetY = None
        self.offsetZ = None
        self.init()

    def init(self, address=0x68):
        success = False
        try:
            self.accelerometer = mpu6050(address)
            success = True
        except Exception as e:
            logging.debug('MPU6050 - not present: {0}'.format(e))
        return success

    def getData(self):
        if self.accelerometer is None:
            if self.init():
                return self._getAccelData()
            else:
                return DEFAULT_ACCEL_READING
        else:
            return self._getAccelData()

    def _getAccelData(self):
        try:
            return self.accelerometer.get_accel_data()
        except Exception as e:
            logging.debug('MPU6050: {0}'.format(e))
            self.accelerometer = None
            return DEFAULT_ACCEL_READING

    def filterData(self, data):
        if self.offsetX != None:
            #do stuff here to add offset
            return DEFAULT_ACCEL_READING
        else:
            return data

    def offsetData(self, data):
        self.offsetX = data.x
        self.offsetY = data.y
        self.offsetZ = data.z

if __name__ == '__main__':
    mpu = cc_i2c_accel_MPU6050()
    print(mpu.getData())
import cc_configuration

from mpu6050 import mpu6050

class cc_i2c_accel_MPU6050:
    def __init__(self):
        self.accelerometer = None
        self.offsetX = None
        self.offsetY = None
        self.offsetZ = None

    def initAccel(self, address=0x68):
        self.accelerometer = mpu6050(address)

    def getData(self):
        return self.accelerometer.get_accel_data()

    def filterData(self, data):
        if self.offsetX != None:
            #do stuff here to add offset
            newData = {'x': 0, 'y': 0, 'z': 0}
            return newData
        else:
            return data

    def offsetData(self, data):
        self.offsetX = data.x
        self.offsetY = data.y
        self.offsetZ = data.z
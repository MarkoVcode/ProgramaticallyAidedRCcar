import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

UDP_SERVER_ADDRESS = 'localhost'
UDP_SERVER_PORT = 10000
UPDATE_SENSORS_EVERY_MS = 30
CAR_THROTTLE_PWM_CHANNEL = 2
CAR_STEER_PWM_CHANNEL = 3
KEEP_THROTTLE_PRESSED_MS = 200

BATTERY_VOLTAGE_MAX = 8.4
BATTERY_VOLTAGE_MIN = 7.0

#controll
DIR_MAX_POSITION = 5
DIR_MIN_POSITION = -5
THR_FORWARD_MAX = 1
THR_BACKWARD_MAX = -1

PI_CAMERAS = ['/dev/camerafront','/dev/cameraback']

SENSORS_FOR_FAILED_CONNECTION = {}
#    'sensors': }
#sensors['accel']['x']
#sensors['system']['core_temp']

def isHardwareSupported():
    if os.environ.get('HOME') == '/home/pi':
        return True
    else:
        return False
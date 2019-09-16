import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

UDP_SERVER_ADDRESS = 'localhost'
UDP_SERVER_PORT = 10000
UPDATE_SENSORS_EVERY_MS = 30
CAR_THROTTLE_PWM_CHANNEL = 2
CAR_STEER_PWM_CHANNEL = 3
KEEP_THROTTLE_PRESSED_MS = 200


def isHardwareSupported():
    if os.environ.get('HOME') == '/home/pi':
        return True
    else:
        return False
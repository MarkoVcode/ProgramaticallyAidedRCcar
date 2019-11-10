import os

VECHICLE_ID = 1

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

UDP_SERVER_ADDRESS = 'localhost'
UDP_SERVER_PORT = 10000
UDP_SERVER_PID_FILE = 'server.pid'
UDP_SERVER_WAIT_FOR_WIFI_SEC = 80
UDP_SERVER_DISPLAY_UPDATE_EVERY_SEC = 1

UPDATE_SENSORS_EVERY_MS = 30
CAR_THROTTLE_PWM_CHANNEL = 2
CAR_STEER_PWM_CHANNEL = 3
KEEP_THROTTLE_PRESSED_MS = 200
KEEP_KEY_PRESSED_MS = 100

BATTERY_VOLTAGE_MAX = 8.4
BATTERY_VOLTAGE_MIN = 6.8
BATTERY_VOLTAGE_WARN = 7.2
BATTERY_VOLTAGE_CRIT = 7.0

METRICS_ON_CLOUD_ENABLED = True
#METRICS_ON_CLOUD_URL = "wss://metrics-on-cloud.appspot.com/chat"
METRICS_ON_CLOUD_URL = "ws://127.0.0.1:8081/chat"
#METRICS_ON_CLOUD_URL = "ws://10.0.2.141:8081/chat"

METRICS_CLOUD_UPDATE_EVERY_SEC = 0.01

CAMERAS_LIST = ("/dev/camerafback", "/dev/cameraffront", "/dev/camerafront", "/dev/video0", "/dev/video1", "/dev/video3")

#controll
DIR_MAX_POSITION = 5
DIR_MIN_POSITION = -5
THR_FORWARD_MAX = 1
THR_BACKWARD_MAX = -1

PROXYMITY_SENSOR_UART = "/dev/tty0"
PROXYMITY_SENSOR_UART_SPEED = 9600

def isHardwareSupported():
    if os.environ.get('HOME') == '/home/pi':
        return True
    else:
        return False
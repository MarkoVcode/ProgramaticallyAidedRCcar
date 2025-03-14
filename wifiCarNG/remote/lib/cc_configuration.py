import os

CONTROLLER_WS = 'ws://192.168.50.217:6689'

def isHardwareSupported():
    if os.environ.get('HOME') == '/home/pi':
        return True
    else:
        return False
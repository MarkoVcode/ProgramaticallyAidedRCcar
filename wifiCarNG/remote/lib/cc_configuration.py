import os

CONTROLLER_WS = 'ws://127.0.0.1:6689'

def isHardwareSupported():
    if os.environ.get('HOME') == '/home/pi':
        return True
    else:
        return False
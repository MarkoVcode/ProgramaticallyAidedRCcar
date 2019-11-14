#!/usr/bin/python
import logging
import socket
import subprocess
import cc_configuration

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

#try this
#sudo iwlist wlan0 scan | egrep "Cell|ESSID|Signal|Rates"
#https://rasspberrypi.wordpress.com/2012/09/09/wifi-tools-for-raspberry-pi/
#implement method here with intent to not be executed too freq.

class cc_wifi:
    def __init__(self):
        self.wifidata = {}

    def fetchAP(self):
        cmd =["nmcli -f SSID,ACTIVE,BARS dev wifi list | awk '$2 ~ /yes/ {print $3 \";\" $1}'"]
        addressx = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = addressx.communicate()
        return out

    def fetchAPR_Pi(self):
        cmd =["iwgetid"]
        address = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = address.communicate()
        return out.replace(":", ";")

    def getWIFIStatus(self):
        self.wifidata['IP'] = "192.168.199.46"
        self.wifidata['AP'] = "MYAp"
        linkInfo = {}
        linkInfo['Quality'] = 6
        linkInfo['Level'] = 6
        linkInfo['Noise'] = 6
        self.wifidata['Link'] = linkInfo
        return self.wifidata

    def fetchIP(self):
        address = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('arduino.cc', 0))
            address=s.getsockname()[0]
        except Exception as e:
            logging.debug('Problem with fetching IP. Defaulting to localhost: {0}'.format(e))
            address='localhost'
        return address

    def fetchNetworkData(self):
        if cc_configuration.isHardwareSupported():
            return self.fetchIP() + ";" + self.fetchAPR_Pi()
        else:
            return self.fetchIP() + ";" + self.fetchAP()

if __name__ == '__main__':
    cc_wifi = cc_wifi()
    print(cc_wifi.fetchNetworkData())

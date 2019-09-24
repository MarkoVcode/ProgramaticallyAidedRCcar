#!/usr/bin/python
import socket
import subprocess
import cc_configuration

class cc_wifi:
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

    def fetchIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('arduino.cc', 0))
        address=s.getsockname()[0]
        return address

    def fetchNetworkData(self):
        if cc_configuration.isHardwareSupported():
            return self.fetchIP() + ";" + self.fetchAPR_Pi()
        else:
            return self.fetchIP() + ";" + self.fetchAP()

if __name__ == '__main__':
    cc_wifi = cc_wifi()
    print(cc_wifi.fetchNetworkData())

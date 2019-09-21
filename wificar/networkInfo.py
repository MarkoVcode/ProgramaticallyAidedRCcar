#!/usr/bin/python
import socket
import subprocess
import gameConfig

def fetchAP():
    cmd =["nmcli -f SSID,ACTIVE,BARS dev wifi list | awk '$2 ~ /yes/ {print $3 \";\" $1}'"]
    address = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = address.communicate()
    return out

def fetchAPR_Pi():
    cmd =["iwgetid"]
    address = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = address.communicate()
    return out.replace(":", ";")

def fetchIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('arduino.cc', 0))
    address=s.getsockname()[0]
    return address

def fetchNetworkData():
    if gameConfig.isHardwareSupported():
        return fetchIP() + ";" + fetchAPR_Pi()
    else:
        return fetchIP() + ";" + fetchAP()

#print fetchNetworkData()

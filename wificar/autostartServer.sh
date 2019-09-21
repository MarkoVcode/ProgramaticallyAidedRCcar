#!/bin/bash 

cd /home/pi/ProgramaticallyAidedRCcar/wificar/
git pull
./UDPIOServer.py </dev/null &>/dev/null &
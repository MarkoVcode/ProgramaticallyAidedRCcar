#!/bin/bash 

./UDPIOServer.py > /dev/null 2>&1 &
./camera.py
./stopServer.sh
#screen -d -m -S UDPServer ./startServer.sh

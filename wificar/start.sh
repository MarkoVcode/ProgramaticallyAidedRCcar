#!/bin/bash 

screen -S UDPServer -d -m ./UDPIOServer.py & echo $! > server.pid
#screen -S UDPServer -d -m './UDPIOServer.py > /dev/null 2>&1 & echo $! > server.pid'
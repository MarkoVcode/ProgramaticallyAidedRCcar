#!/usr/bin/python
import threading
import os
import time
import logging
import random
import Queue
import socket
import sys
import gameConfig
import hardware
import networkInfo

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (gameConfig.UDP_SERVER_ADDRESS, gameConfig.UDP_SERVER_PORT)
sock.bind(server_address)

logging.debug('Starting up on %s port %s' % server_address)

hw = hardware.HardwareStrategy()

BUF_SIZE = 20
q = Queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name
        self.firstRun = True

    def run(self):
        while True:
            if self.firstRun:
                systemNetworkInfo = "i2c:oled:" + networkInfo.fetchNetworkData()
                q.put(systemNetworkInfo)
                logging.debug('Putting ' + str(systemNetworkInfo)  
                                + ' : ' + str(q.qsize()) + ' items in queue')
                self.firstRun = False
            time.sleep(0.001)
            logging.debug('Awaiting for the messages. ' + str(q.qsize()) + ' items in queue')
            data, address = sock.recvfrom(4096)
            instElems = data.split(":",)
            if instElems[0] == "read":
                sensors = hw.fetchSensors(instElems[1])
                sent = sock.sendto(str(sensors), address)
                logging.debug('Returning sensors: ' + str(sensors))
            else:
                if not q.full():
                    q.put(data)
                    logging.debug('Putting ' + str(data)  
                                + ' : ' + str(q.qsize()) + ' items in queue')
                if data:
                    sent = sock.sendto(data, address)
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            time.sleep(0.001)
            if not q.empty():
                intId = hw.interactionID()
                item = q.get()
                logging.debug(intId + ' Getting ' + str(item) 
                              + ' : ' + str(q.qsize()) + ' items in queue')
                hw.executeIOInteraction(intId, str(item))
            hw.readAllSensorsCycle()
        return

def writePidFile():
    pid = str(os.getpid())
    f = open('server.pid', 'w')
    f.write(pid)
    f.close()

if __name__ == '__main__':
    writePidFile()
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')
    p.start()
    c.start()
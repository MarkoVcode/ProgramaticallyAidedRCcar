#!/usr/bin/python
import threading
import os
import time
import logging
import random
import Queue
import socket
import sys

import lib.cc_configuration as gameConfig
from lib.cc_wifi import cc_wifi
from lib.cc_sensors import cc_sensors

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (gameConfig.UDP_SERVER_ADDRESS, gameConfig.UDP_SERVER_PORT)

networkInfo = cc_wifi()
hw = cc_sensors()

BUF_SIZE = 20
q = Queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
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

class NetworkMonitor(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(NetworkMonitor,self).__init__()
        self.target = target
        self.name = name

        #For network info displayed
        self.firstRun = True
        self.startTime = time.time()
        self.lastDisplayUpdate = 0
        return

    def run(self):
        while True:
            time.sleep(gameConfig.UDP_SERVER_DISPLAY_UPDATE_EVERY_SEC)
            self.netInfo()
        return

    def netInfo(self):
        ##Add users session monitor here and potentially queues info??
        if self.firstRun:
            if time.time() - self.startTime < gameConfig.UDP_SERVER_WAIT_FOR_WIFI_SEC:
                wifi = networkInfo.fetchNetworkData()
                if "localhost" in wifi:
                    self.displayOLED(self.netWaitingMessage())
                else:
                    self.displayOLED(wifi)
                    self.firstRun = False
            else:
                self.displayOLED(networkInfo.fetchNetworkData())
                self.firstRun = False
    
    def netWaitingMessage(self):
        if time.time() % 2 < 1:
            return "- wifi scan -"
        else:
            return "* wifi scan *"

    def displayOLED(self, message):
        messageToDisplay = "i2c:oled:" + message
        q.put(messageToDisplay)
        logging.debug('Putting ' + str(messageToDisplay)  
                        + ' : ' + str(q.qsize()) + ' items in queue')

def writePidFile():
    pid = str(os.getpid())
    f = open(gameConfig.UDP_SERVER_PID_FILE, 'w')
    f.write(pid)
    f.close()

if __name__ == '__main__':
    #writePidFile()
    try:
        sock.bind(server_address)
        logging.debug('Starting up on %s port %s' % server_address)
        p = ProducerThread(name='producer')
        c = ConsumerThread(name='consumer')
        n = NetworkMonitor(name='network')
        p.start()
        c.start()
        n.start()
    except:
        logging.debug('Can not start. Socket in use.')
        exit    

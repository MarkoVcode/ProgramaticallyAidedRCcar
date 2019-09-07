import threading
import time
import logging
import random
import Queue
import socket
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
logging.debug('Starting up on %s port %s' % server_address)

BUF_SIZE = 50
q = Queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            logging.debug('Awaiting for the messages. ' + str(q.qsize()) + ' items in queue')
            data, address = sock.recvfrom(4096)
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
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item) 
                              + ' : ' + str(q.qsize()) + ' items in queue')
        return

if __name__ == '__main__':
    
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    c.start()
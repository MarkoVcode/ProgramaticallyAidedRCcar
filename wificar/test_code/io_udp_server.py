from Queue import Queue
import socket
import sys

#import Adafruit_PCA9685

#pwm = Adafruit_PCA9685.PCA9685()
#pwm.set_pwm_freq(60)
    #pwm.set_pwm(3, 0, x_change)
    #pwm.set_pwm(2, 0, y_change)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
enclosure_queue = Queue()

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    enclosure_queue.put(data)
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    enclosure_queue.join()
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
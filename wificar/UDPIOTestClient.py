import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
#mesages from keyboard
message = 'i2c:pwm:dir:0'
#message = 'i2c:pwm:dir:-5'
#message = 'i2c:pwm:dir:5'
#message = 'i2c:pwm:thr:0'
#message = 'i2c:pwm:thr:1'
#message = 'gpio:pin:ls1:0'  # lights short (including back)
#message = 'gpio:pin:ll2:0'  # lights long (both lights)
#message = 'gpio:pin:indl:0'   #  indicator left  not exposed on UI
#message = 'gpio:pin:indr:0'    # indicator right not exposed on UI
#message = 'gpio:pin:horn:0'    # audio warning
#message = 'gpio:pin:horn:1'
#message from the web app
#message = 'gpio:pin:engaged:0' # engaged warning LED
#message = 'i2c:oled:msg:192.168.0.33;q2;engaged'


try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
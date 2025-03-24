import socket
import json
import random

def server_program():
    print("This Host: " + str(socket.gethostname()))
    # get the hostname

    host = 'localhost'
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            elif data == 'telem':
            #print("from connected user: " + str(data))
                message = {
                                "type": "button_down",
                                "joystick_id": "dddd",
                                "button": random.randint(0, 100)
                            }
            elif data == 'other':
                message = {
                                "button": random.randint(0, 100)
                            }
            else:
                message = {
                                "nothing": random.randint(0, 100)
                            }
            data = json.dumps(message)
            conn.send(data.encode())
            message = '' # send data to the client
        print("Disconnected!")
        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
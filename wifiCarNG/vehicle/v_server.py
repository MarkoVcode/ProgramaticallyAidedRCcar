import socket
import threading
import json
import random

HOST = '127.0.0.1'  # Loopback address; use your server’s IP if needed.
PORT = 5004         # Arbitrary non-privileged port.

def handle_client(conn, addr):
    print(f"[SERVER] New connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"[SERVER] {addr} disconnected.")
            break
        data_in = data.decode()
        print(f"[SERVER] Received from client {addr}: {data_in}")
        try:
            data = json.loads(data_in)
            #controller data here
            #parse data and set controlls
            print("Controller:", data)
            message = "controll processed"
            conn.sendall(message.encode())
        except json.JSONDecodeError:
            print("Request for:", data_in)
        # Here you can decide what to send back.
        # For demonstration, let's just echo a confirmation message.
            message = {
                        "type": "button_down",
                        "joystick_id": "dddd",
                        "button": random.randint(0, 100)
                    }
        #input("[SERVER] Enter message to send: ")
            conn.sendall(json.dumps(message).encode())
    conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[SERVER] Listening on {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        # Use a thread to handle each client connection
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"[SERVER] Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()

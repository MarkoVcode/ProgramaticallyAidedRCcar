import socket

HOST = '127.0.0.1'  # IP or hostname of the server
PORT = 5004        # Must match the server’s port

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

    try:
        while True:
            msg = input("[CLIENT] Enter message (type 'exit' to quit): ")
            if msg.lower() == 'exit':
                print("[CLIENT] Closing connection.")
                break

            # Send a message to the server
            client_socket.sendall(msg.encode())

            # Receive and display the server's response
            data = client_socket.recv(1024)
            if not data:
                print("[CLIENT] Server disconnected.")
                break
            print(f"[CLIENT] Received from server: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()

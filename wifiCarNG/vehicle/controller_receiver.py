import asyncio
import websockets
import json
import lib.cc_configuration as app_config

# The handler for each connected client
async def handle_connection(websocket):
    print("Client connected!")

    try:
        async for message in websocket:
            # The client should be sending JSON, so let's parse it
            try:
                data = json.loads(message)
                print("Received:", data)
            except json.JSONDecodeError:
                print("Received non-JSON message:", message)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")

async def main(host='127.0.0.1', port=6689):
    print(f"Starting WebSocket server on ws://{host}:{port} ...")
    async with websockets.serve(
            handle_connection,
            host,
            port,
            ping_interval=None,
            ping_timeout=None
        ):
        print("Server is up and running. Waiting for connections...")
        # Run forever
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main(app_config.CONTROLLER_LISTENER_WS_IP, app_config.CONTROLLER_LISTENER_WS_PORT))
    except KeyboardInterrupt:
        print("Server stopped by user.")


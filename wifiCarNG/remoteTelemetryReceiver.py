import asyncio
import websockets
import json

async def connect_and_receive():
    uri = "ws://localhost:8765/"
    async with websockets.connect(uri) as websocket:
        # Wait to receive the message from the server
        raw_message = await websocket.recv()
        data = json.loads(raw_message)
        print("Received JSON data:", data)

if __name__ == "__main__":
    asyncio.run(connect_and_receive())


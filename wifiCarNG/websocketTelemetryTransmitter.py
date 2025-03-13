import asyncio
import websockets
import random
import json

async def handler(websocket, path):
    """
    This function is called whenever a new client connects.
    It sends two random numbers in JSON format to the client.
    """
    data = {
        "number1": random.randint(1, 100),
        "number2": random.randint(1, 100)
    }
    # Convert dictionary to JSON string
    message = json.dumps(data)
    
    # Send the JSON to the client
    await websocket.send(message)
    # Optional: close the connection after sending
    # await websocket.close()

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        # Keep the server running forever
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())


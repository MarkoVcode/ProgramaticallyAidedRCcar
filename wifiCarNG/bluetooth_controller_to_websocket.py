import sys
import asyncio
import json
import pygame
import websockets

async def main(websocket_uri):
    # 1. Initialize Pygame and Joystick
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No Bluetooth (or other) controller detected. Please pair/connect your gamepad and try again.")
        return

    # For simplicity, just use the first controller found
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Found controller: {joystick.get_name()}")

    # 2. Connect to the WebSocket server
    print(f"Connecting to WebSocket: {websocket_uri}")
    async with websockets.connect(
            websocket_uri,
            ping_interval=30,     # send a ping every 30 seconds
            ping_timeout=30       # wait 30 seconds for a pong before closing
        ) as websocket:
        print("WebSocket connection established!")

        # 3. Main event loop
        running = True
        clock = pygame.time.Clock()

        while running:
            # Process Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Joystick button pressed
                elif event.type == pygame.JOYBUTTONDOWN:
                    message = {
                        "type": "button_down",
                        "joystick_id": event.joy,
                        "button": event.button
                    }
                    await websocket.send(json.dumps(message))
                    print("Sent:", message)

                # Joystick button released
                elif event.type == pygame.JOYBUTTONUP:
                    message = {
                        "type": "button_up",
                        "joystick_id": event.joy,
                        "button": event.button
                    }
                    await websocket.send(json.dumps(message))
                    print("Sent:", message)

                # Joystick axis motion (e.g., thumbsticks)
                elif event.type == pygame.JOYAXISMOTION:
                    # event.value is in the range [-1.0, 1.0]
                    message = {
                        "type": "axis_motion",
                        "joystick_id": event.joy,
                        "axis": event.axis,
                        "value": round(event.value, 3)  # limit precision
                    }
                    await websocket.send(json.dumps(message))
                    print("Sent:", message)

                # Joystick hat (D-pad) motion
                elif event.type == pygame.JOYHATMOTION:
                    # event.value is a tuple (x, y) where x,y in {-1, 0, 1}
                    message = {
                        "type": "hat_motion",
                        "joystick_id": event.joy,
                        "hat": event.hat,
                        "value": event.value
                    }
                    await websocket.send(json.dumps(message))
                    print("Sent:", message)

            # Avoid maxing out CPU - limit to ~60 checks per second
            clock.tick(30)
            # await websocket.send(json.dumps({"type": "keepAlive"}))
        # Clean up after loop ends
        joystick.quit()
        pygame.quit()
        print("Disconnected from WebSocket and closed Pygame.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bluetooth_controller_to_websocket.py ws://<HOST>:<PORT>")
        sys.exit(1)

    websocket_url = sys.argv[1]
    try:
        asyncio.run(main(websocket_url))
    except KeyboardInterrupt:
        print("User interrupted. Exiting...")
    except Exception as e:
        print(f"Error: {e}")


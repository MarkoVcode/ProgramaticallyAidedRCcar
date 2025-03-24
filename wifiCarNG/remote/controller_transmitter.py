import sys
import asyncio
import json
import pygame
import websockets
import lib.cc_configuration as app_config
from time import sleep

async def main(disable_ws, websocket_uri):
    # 1. Initialize Pygame and Joystick
    #pygame.init()
    joystick_count = 0
    joystick_once = True
    while joystick_count == 0:
        pygame.init()
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            sleep(0.5)
            pygame.quit()
            if joystick_once:
                print("No Bluetooth (or other) controller detected. Please pair/connect your gamepad and try again.")
                joystick_once = False
    # For simplicity, just use the first controller found
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Found controller: {joystick.get_name()}")

    if disable_ws:
        print("Not connecting to websockets!")

        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                await process_joy_event(None, event)

            clock.tick(25)
        # Clean up after loop ends
        joystick.quit()
        pygame.quit()
        print("Closed Pygame.")
    else:   
    # 2. Connect to the WebSocket server
        print(f"Connecting to WebSocket: {websocket_uri}")
        async with websockets.connect(
                websocket_uri,
                ping_interval=30,     # send a ping every 30 seconds
                ping_timeout=30       # wait 30 seconds for a pong before closing
            ) as websocket:
            print("WebSocket connection established!")

            running = True
            clock = pygame.time.Clock()

            while running:
                for event in pygame.event.get():
                    await process_joy_event(websocket, event)

                clock.tick(25)
            # Clean up after loop ends
            joystick.quit()
            pygame.quit()
            print("Disconnected from WebSocket and closed Pygame.")

async def process_joy_event(websocket, event):
    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.JOYBUTTONDOWN:
        message = {     
                        "joy_id": event.joy,
                        "type": "button_down",
                        "button": event.button
                    }
        await send_message(websocket, message)

    elif event.type == pygame.JOYBUTTONUP:
        message = {     
                        "joy_id": event.joy,
                        "type": "button___up",
                        "button": event.button
                    }
        await send_message(websocket, message)

    elif event.type == pygame.JOYAXISMOTION:
                    # event.value is in the range [-1.0, 1.0]
        message = {
                        "joy_id": event.joy,
                        "type": "axis_motion",
                        "axis__": event.axis,
                        "value": round(event.value, 3)  # limit precision
                    }
        await send_message(websocket, message)

    elif event.type == pygame.JOYHATMOTION:
                    # event.value is a tuple (x, y) where x,y in {-1, 0, 1}
        message = {
                        "joy_id": event.joy,
                        "type": "hat__motion",
                        "hat___": event.hat,
                        "value": event.value
                    }
        await send_message(websocket, message)

async def send_message(websocket, message):
    if websocket != None:
        await websocket.send(json.dumps(message))
        print("Sent:", message)
    else:
        print(message)

if __name__ == "__main__":
    websocket_url = ''
    disable_ws = False
    if len(sys.argv) < 2:
        print("Usage: python remote_controller_transmitter.py transmit ws://<HOST>:<PORT>")
        print("Usage: python remote_controller_transmitter.py donotsend")
        print("No ws address provided - sending using the one from the config")
        print(app_config.CONTROLLER_WS)
        websocket_url = app_config.CONTROLLER_WS
        #sys.exit(1)
    else:
        if sys.argv[1] == 'donotsend':
            disable_ws = True
        elif sys.argv[1] == 'transmit':
            disable_ws = False
            websocket_url = sys.argv[2]
    while True:    
        try:
            asyncio.run(main(disable_ws, websocket_url))
        except KeyboardInterrupt:
            print("User interrupted. Exiting...")
        except Exception as e:
            print(f"Error: {e}")
            print("Trying to reconnect...")
            sleep(0.8)


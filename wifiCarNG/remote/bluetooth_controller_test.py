import pygame

def main():
    # Initialize Pygame
    pygame.init()
    pygame.joystick.init()

    # Attempt to detect joysticks (controllers) connected
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No controller detected. Make sure your Bluetooth controller is paired and recognized by your OS.")
    else:
        # Initialize each detected joystick
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            print(f"Detected controller #{i} named '{joystick.get_name()}'")

    # Create a basic window to keep the program running
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Bluetooth Controller Test")

    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Joystick button pressed
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick {event.joy} Button {event.button} pressed")

            # Joystick button released
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Joystick {event.joy} Button {event.button} released")

            # Joystick axis motion (e.g., thumbsticks)
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Joystick {event.joy} Axis {event.axis} moved to {event.value:.2f}")

            # Joystick hat motion (some controllers have directional pad hats)
            elif event.type == pygame.JOYHATMOTION:
                print(f"Joystick {event.joy} Hat {event.hat} moved to {event.value}")

        pygame.display.flip()  # Update the window surface

    # Clean up on exit
    pygame.quit()

if __name__ == "__main__":
    main()


import pygame

pygame.init()
pygame.mixer.quit()  # performance fix
size = ( 16, 16 )
screen = pygame.display.set_mode(size)
pygame.display.set_caption("High CPU")

clock = pygame.time.Clock()

run=True
while run:

    print("Rendering...")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run=False

    screen.fill((255,255,255))

    # Render
    pygame.display.flip()
    clock.tick(1)

# When done
pygame.quit()
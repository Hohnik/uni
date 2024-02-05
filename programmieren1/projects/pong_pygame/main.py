import sys

import pygame


def main():
    """
    Pong game main function
    """
    pygame.init()
    screen = pygame.display.set_mode(size=(100, 200))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Basic Pygame program")

    while True:  # gameloop
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        pygame.display.update()
        screen.fill("yellow")
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__name__":
    main()

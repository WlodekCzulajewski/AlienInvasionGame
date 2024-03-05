import sys
import pygame


class AlienInvasion:
    """General class responsible for resource managment and functionality of game."""

    def __init__(self):
        """Game initialization and resource creation."""
        pygame.init()

        self.screen = pygame.display.set_mode((2560, 1600))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Launch loop of main game."""
        while True:
            #Waiting to press the button or click the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Show last modified display.
            pygame.display.flip()


if __name__ == "__main__":
    #Create game object and launch it.
    ai = AlienInvasion()
    ai.run_game()


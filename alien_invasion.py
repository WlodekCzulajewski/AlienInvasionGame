import sys
import pygame


class AlienInvasion:
    """General class responsible for resource managment and functionality of game."""

    def __init__(self):
        """Game initialization and resource creation."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien invasion")

        #Define background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Launch loop of main game."""
        while True:
            #Waiting to press the button or click the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Reload display in every loop iteration
            self.screen.fill(bg_color)
            
            #Show last modified display.
            pygame.display.flip()


if __name__ == "__main__":
    #Create game object and launch it.
    ai = AlienInvasion()
    ai.run_game()


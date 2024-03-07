import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """General class responsible for resource managment and functionality of game."""

    def __init__(self):
        """Game initialization and resource creation."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))  #((0, 0), pygame.FULLSCREEN) for fullscreen
        pygame.display.set_caption("Alien invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        """Launch loop of main game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Reaction on events generated by keyboard and mouse."""
        #Waiting to press the button or click the mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Updates images on display and switches to new display."""
        #Reload display in every loop iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Show last modified display.
        pygame.display.flip()


if __name__ == "__main__":
    #Create game object and launch it.
    ai = AlienInvasion()
    ai.run_game()


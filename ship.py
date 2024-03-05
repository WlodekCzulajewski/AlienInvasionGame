import pygame


class Ship:
    """Class responsible for spaceship functionality."""

    def __init__(self, ai_game):
        """Initialization of spaceship and its starting position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load spaceship image and load its rectangle.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Every new spaceship starts at the bottom of a screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display spaceship at his current position."""
        self.screen.blit(self.image, self.rect)


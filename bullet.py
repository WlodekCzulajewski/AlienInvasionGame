import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class responsible for managment of bullets shot by space ship."""

    def __init__(self, ai_game):
        """Create object bullet at the current space ship position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create rect of bullet in position (0, 0), and then define for it correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Position of bullet is stored in float type value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet on screen."""
        #Actualization of bullet position.
        self.y -= self.settings.bullet_speed
        #Actualization of bullet rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on display."""
        pygame.draw.rect(self.screen, self.color, self.rect)


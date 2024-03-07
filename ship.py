import pygame


class Ship:
    """Class responsible for spaceship functionality."""

    def __init__(self, ai_game):
        """Initialization of spaceship and its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load spaceship image and load its rectangle.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Every new spaceship starts at the bottom of a screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
        #Position of spaceship is saved in float type.
        self.x = float(self.rect.x)

        #Options of movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualization of ships position based on option of movement."""
        #Actualization of ships X location, but not its rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        #Actualization of rect X location, based on value of self x.
        self.rect.x = self.x

    def blitme(self):
        """Display spaceship at his current position."""
        self.screen.blit(self.image, self.rect)


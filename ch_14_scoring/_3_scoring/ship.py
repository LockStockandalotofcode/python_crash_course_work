""""Ship class for alien invasion game."""
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship and get its rect.
        # rect stands for rectangular coordinates (x, y, width, height), in software/ graphics
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags; start with a ship thats not moving.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
            """ReCenter ship on the screen."""
            self.rect.midbottom = self.screen_rect.midbottom
            self.x = float(self.rect.x)
            
    def update(self):
        """Update ship's position based on the movement flags."""
        # update ship's x value not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        # Only integer portion is assigned to self.rect.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
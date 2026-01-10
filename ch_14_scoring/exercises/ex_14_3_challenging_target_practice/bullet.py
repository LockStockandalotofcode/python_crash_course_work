import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from the ship."""

    def __init__(self, tp_game):
        """Create a bullet object at ship's current position."""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct rect position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = tp_game.ship.rect.midleft

        # Store bullet's x coordinate as float to control its horizontal speed.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally on screen."""
        # Update exact position
        self.x += self.settings.bullet_speed
        # Update rect attribute
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Draw bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
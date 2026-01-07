"""module to manage raindrop behaviour in raindrops game."""
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to manage a single raindrop's behaviour."""
    def __init__(self, rd_game):
        """Initialise raindrop and set its startings position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and set its rect attribute to determine its starting position later
        self.image = pygame.image.load('images/raindrop_icon.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop at the top left of the screen with some gap above and on left to ensure visibility
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position as float value
        # since we'll focus only on its vetical speed
        self.y = float(self.rect.y)

    def update(self):
        """Move raindrop down the screen."""
        self.y += self.settings.raindrop_drop_speed
        self.rect.y = self.y

        # If raindrop reaches bottom of screen, reset its position to top
        if self.rect.bottom >= self.screen.get_rect().bottom:
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star on screen."""
    def __init__(self, s_game):
        """Initialise a star and set its starting position."""
        super().__init__()
        self.screen = s_game.screen

        # Load the star and get its rect attribute
        self.image = pygame.image.load('images/star_icon.png')
        self.rect = self.image.get_rect()

        # Start each new star at top left corner on screen.
        # at a gap of one star's dimensions above and on left to ensure visibility
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
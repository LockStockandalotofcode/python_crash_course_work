import pygame
from pygame.sprite import Sprite

class Goku(Sprite):
    """A class to represnt goku character."""

    def __init__(self, ss_game):
        """Initialise goku and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load goku image and set rect attribute
        self.image = pygame.image.load('images/goku_image.bmp')
        self.rect = self.image.get_rect()

        # Set starting position of goku at top right corner
        #  goku comes with some gap above and on right to ensure visibility
        # self.rect.x = self.screen.get_rect().width - self.rect.width
        # self.rect.y = self.rect.height

        # Store goku's exact position 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move single goku up or down."""
        self.y -= 5*self.settings.goku_speed 
        self.rect.y = self.y

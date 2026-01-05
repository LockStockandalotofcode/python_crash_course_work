"""Module to manage behaviour of character image on screen."""

import pygame

class Goku:
    """A class to manage goku character."""

    def __init__(self, main_game):
        """Initialise the character, and set its starting position"""

        self.screen = main_game.screen
        self.screen_rect = main_game.screen.get_rect()

        # Load the character image and get its rect attribute.
        self.image = pygame.image.load('images/goku_image.bmp')
        self.rect = self.image.get_rect()

        # set staring position for character on the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at location."""
        self.screen.blit(self.image, self.rect)
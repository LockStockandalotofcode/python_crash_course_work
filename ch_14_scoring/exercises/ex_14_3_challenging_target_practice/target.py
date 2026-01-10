"""Target class."""

import pygame

from pygame.sprite import Sprite

class Target(Sprite):
    """A Class to represent a single alien in the group."""

    def __init__(self, tp_game):
        """Initialise the target and set its starting position."""
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings

        # create a target rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        # Store target's exact vertical position.
        self.y = float(self.rect.y)

    def center_target(self):
        # REcenter target on screen.
        self.rect.midright = self.screen_rect.midright

        # Store target's exact vertical position.
        self.y = float(self.rect.y)
    
    def check_edges(self):
        """Return true if target is at top or bottom edge."""
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

    def update(self):
        """Move target up or down."""
        self.y += (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y

    def draw_target(self):
        """Draw target on screen."""
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)
"""Ship class for the game."""
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, tp_game):
        """Initialise the ship and set its starting position."""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings

        # Load the ship and get its rect attribute
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Set starting position for ship.
        self.rect.midleft = self.screen_rect.midleft
        # Store y-coordinate as float for exact vertical position to control vertical position
        self.y = float(self.rect.y)

        # Movement flags; game starts with a ship thats not moving
        self.moving_up = False
        self.moving_down = False
    
    def center_ship(self):
            """ReCenter ship on the screen."""
            self.rect.midleft = self.screen_rect.midleft
            self.y = float(self.rect.y)

    def update(self):
        """Update ship's position based on movement flags."""
        # update ship's y-coordinate not rect attribute
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # downward motion is not kept in elif block;

        # update rect y attribute
        self.rect.y = self.y
        

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
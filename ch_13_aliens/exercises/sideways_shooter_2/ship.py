""""Ship class for alien invasion game."""
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship and get its rect.
        # rect stands for rectangular coordinates (x, y, width, height), in software/ graphics
        self.image = pygame.image.load('images/gun_icon.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        # Store a float for ship's exact horizontal position
        self.y = float(self.rect.y)

        # Movement flags; start with a ship thats not moving.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship's position based on the movement flags."""
        # update ship's x value not rect
        if self.moving_up and self.rect.y > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.y <= self.screen_rect.height:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        # Only integer portion is assigned to self.rect.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
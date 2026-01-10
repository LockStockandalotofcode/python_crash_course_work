""""gun class for sideways shooter 2 game."""
import pygame

class Gun:
    """A class to manage the gun."""

    def __init__(self, ss_game):
        """Initialise the gun and set its starting position."""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings

        # Load the gun and get its rect.
        # rect stands for rectangular coordinates (x, y, width, height), in software/ graphics
        self.image = pygame.image.load('images/gun_icon.png')
        self.rect = self.image.get_rect()

        # Start each new gun at the middle of left edge of the screen.
        self.rect.midleft = self.screen_rect.midleft
        # Store a float for gun's exact vertical position
        self.y = float(self.rect.y)

        # Movement flags; start with a gun thats not moving.
        self.moving_up = False
        self.moving_down = False

    def center_gun(self):
        """Center the gun on screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)

    def update(self):
        """Update gun's position based on the movement flags."""
        # update gun's y value not rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.gun_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.gun_speed

        # Update rect object from self.y
        # Only integer portion is assigned to self.rect.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the gun at its current location."""
        self.screen.blit(self.image, self.rect)
        
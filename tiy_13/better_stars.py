import sys

import pygame

from settings import Settings
from star import Star
from random import randint

class StarsGame:
    """Overall class to manage game assets and behaviour of elements."""

    def __init__(self):
        """Initialise the game, create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars Game")

        self.stars = pygame.sprite.Group()
        self._create_grid()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Helper function for main loop: REspond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_grid(self):
        """Create a grid of stars."""
        # make a star and keep adding stars until no more to fit in a row
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < self.settings.screen_height - 3*star_height:
            while current_x < self.settings.screen_width - 2*star_width:
                # Create a star and place it in the row until no room left.
                # introducing randomness in star positions
                add_x = randint(-10, 10)
                add_y = randint(-10, 10)
                # current_x += add_x
                # current_y += add_y
                self._create_star(current_x + add_x, current_y + add_y)
                current_x += 2*star_width

            current_x = star_width
            current_y += star_height*2
        
    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Helper method: Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    sg = StarsGame()
    sg.run_game()
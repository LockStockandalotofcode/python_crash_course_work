"""Main module for raindrops game."""
import sys
import pygame

from settings import Settings
from updated_raindrop import Raindrop

class RaindropsGame:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops game")
        self.raindrops = pygame.sprite.Group()
        self._create_grid()
    
    def run_game(self):
        """Start the main loop for the game,"""
        while True:
            self.check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _update_raindrops(self):
        """Update positions of all raindrops in the grid."""
        self.raindrops.update()
    
    def _create_grid(self):
        """Create a grid of raindrops."""
        # Make a raindrop 
        # Keep adding raindrops until no room left in a row. Spacing between each raindrop is equal to one raindrop width.
        raindrop = Raindrop(self)
        raindrop_height = raindrop.rect.size[1]

        current_y = raindrop_height
        # fill the screen with raindrops row by row
        while current_y < self.settings.screen_height:
            # fill each row with raindrops
            self._create_row_of_raindrops(current_y)
            current_y += 2 * raindrop_height

    def _create_row_of_raindrops(self, y_position):
        """Create a row of raindrops."""
        raindrop = Raindrop(self)
        raindrop_width = raindrop.rect.size[0]

        current_x = raindrop_width
        while current_x < self.settings.screen_width - 2*raindrop_width:
            # create a raindrop and place it in the row until no room left
            self._create_raindrop(current_x, y_position)
            current_x += 2 * raindrop_width

    def _create_raindrop(self, x_position, y_position):
        """Create a single and place it in the grid."""
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        new_raindrop.y = y_position
        self.raindrops.add(new_raindrop)
    
    def _update_screen(self):
        """Helper function to main loop Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # """Make a game instance and run the game."""
    rd_game = RaindropsGame()
    rd_game.run_game()
import sys

import pygame

from settings import Settings

class Keys:
    """Class to manage the game."""

    def __init__(self):
        """Initialise game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((600, 400))
        self.bg_color = (0, 100, 100)
        pygame.display.set_caption("Keys Game")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # print(pygame.key.get_focused())
                    print(f"{event.key}")
                    if event.key == pygame.K_q:
                        sys.exit()

            self._update_screen()
            self.clock.tick(60)
    
    def _update_screen(self):
        """Update images and elements on screen and flip to new screen each time the loop executes."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    game = Keys()
    game.run_game()
"""blue sky main module."""
import pygame
import sys

class VikusGame:
    """generate a blue background"""

    def __init__(self):
        """Initiallize game, add game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Viku's game")

        # set background color - blue
        self.bg_color = (0, 0, 230)

    def run_game(self):
        """Start main loop for game, add close window functionality."""
        while True:
            # Watch for keyboard and mouse movements
            # for loop is the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Create a game instance, and run the game.
    game = VikusGame()
    game.run_game()
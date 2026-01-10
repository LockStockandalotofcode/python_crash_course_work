class GameStats:
    """Track statistics for sideways shooter game."""

    def __init__(self, ss_game):
        """Initialise statistics."""
        self.settings = ss_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.guns_left = self.settings.guns_limit

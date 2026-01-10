class GameStats:
    """Track statistics for game."""

    def __init__(self, tp_game):
        """Initialise statistics."""
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialise stats that can change during the game."""
        self.attempts_left = self.settings.miss_limit
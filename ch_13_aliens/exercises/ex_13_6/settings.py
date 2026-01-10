class Settings:
    """A class to store all settings for game - sideways shooter 2 ."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # gun settings
        self.gun_speed = 5.0
        self.guns_limit = 3

        # Bullets settings
        self.bullet_speed = 5.0
        self.bullet_height = 3
        self.bullet_width = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Goku settings
        self.goku_speed = 1.0

        self.army_sliding_speed = 100
        # army_direction of 1 represents down; -1 represents up
        self.army_direction = 1

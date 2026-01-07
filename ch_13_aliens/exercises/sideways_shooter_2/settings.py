class Settings:
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullets settings
        self.bullet_speed = 2.0
        self.bullet_height = 300
        self.bullet_width = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Goku settings
        self.goku_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left
        self.army_direction = 1
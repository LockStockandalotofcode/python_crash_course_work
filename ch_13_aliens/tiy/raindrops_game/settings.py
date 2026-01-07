class Settings:
    """A class to store all settings for Raindrops game."""
    def __init__(self):
        """Initialise game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192,255,254)
        
        # Raindrop's settings
        self.raindrop_drop_speed = 1.0
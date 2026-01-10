class Settings:
    """A class to stpre all settings for the game."""

    def __init__(self):
        """Initialise game's static settings"""

        # Screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Bullets settings
        self.bullet_width = 15
        self.bullet_height = 100
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # bullets appearing on screen at once not more than 3

        # Target settings 
        self.target_width = 50
        self.target_height = 100
        self.target_color = (0, 135, 0)
        
        # self.targets_limit = 1 # targets allowed # game runs for (targets_limit + 1) times
        # miss limit
        self.miss_limit = 5

        # how quickly the game speeds up
        self.speedup_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        # Ship settings
        self.ship_speed = 5
        self.bullet_speed = 10
        self.target_speed = 1.0

        self.target_direction = 1 # target direction o 1 represents down
    
    def increase_speed_settings(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale

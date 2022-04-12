class Settings:
    """Class to store all settings for alien Invasion"""
    def __init__(self):
        """screen settings"""
        self.bg_color = (30, 30, 30)
        self.screen_width = 1200
        self.screen_height = 600
        """bullet Settings"""
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 100, 0)
        """player settings"""
        self.lives = 3
        self.score = 0
        self.alien_speed = 1
        

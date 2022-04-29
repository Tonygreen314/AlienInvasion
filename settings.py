class Settings:
    """Class to store all settings for alien Invasion"""
    def __init__(self):
        """screen settings"""
        self.bg_color = (30, 30, 30)
        self.screen_width = 1200
        self.screen_height = 600
        """bullet Settings"""
        self.bullet_speed = 20
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (100, 255, 0)
        """player settings"""
        self.lives = 3
        self.score = 0
        self.alien_speed = 2
        self.points = 1
        self.boss_kill = False
        self.bullet_limit = 5
        self.direction = 1
        self.drop_speed = 10
        self.game_on = True
        self.wave_number = 1
        self.difficulty_scale = float(1 + self.wave_number * 0.2)

import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """class of bullets that are fired from the ship"""
    def __init__(self, settings, screen, ship):
        """this initializes the bullet and tacks the position that it is on the screen"""
        super(Bullets, self).__init__()
        self.screen = screen
        """create the bullet rectangle"""
        """creates a rectangular bullet at 0,0"""
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        """move the bullet to the center/top of the ship"""
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        """stores the bullets position as a decimal value"""
        self.y = float(self.rect.y)
        """assign the color to the bullets"""
        self.color = settings.bullet_color
        """assign the speed of the bullets"""
        self.speed = settings.bullet_speed

    def update(self):
        """move the bullets up the screen"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draws the bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

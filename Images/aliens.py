import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        """define attribute screen and settings"""
        self.screen = screen
        self.settings = settings
        """load alien ship image and scale it to fit screen and get rectangular properties"""
        self.image = pygame.image.load('Images/ufo-4778062_1280.png')
        self.image = pygame.transform.scale(self.image, (50, 25))
        self.rect = self.image.get_rect()
        """set starting location"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        """spacing for the fleet"""
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))
        """the moving of the ship"""
        self.speed = settings.alien_speed
        self.direction = 1
        self.drop_speed = settings.drop_speed

    def blitme(self):
        """draws the ship on the screen"""
        """image destination/blit (image being added, location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ move's alien"""
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def check_screen(self):
        # return True if alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right - 1:
            return True
        elif self.rect.left < 1:
            return True

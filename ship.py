import pygame


class Ship:

    """a class to store the information of the ship"""
    def __init__(self, screen, angle):
        self.screen = screen
        self.angle = angle
        """load image of ship and access image data"""
        self.image = pygame.image.load('Images/rocket-6972424_1280.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, self.angle)
        """tells computer to interpret self.image as a rectangle"""
        self.rect = self.image.get_rect()
        """tells computer to interpret the screen as a rectangle"""
        self.screen_rect = screen.get_rect()
        """set starting location of each shop"""
        """ makes the center x values of the ship the same as the center x values of the screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        """makes the bottom of the ship the same as the bottom of the screen"""
        self.rect.bottom = 570
        """stores center_x of ship as a decimal value"""
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        """create movement flag to determine if the ship is moving"""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """draws the ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """updates the movement of the ship by moving it left and or right"""
        if self.moving_right:
            self.center += 3
        if self.moving_left:
            self.center -= 3
        if self.center <= 25:
            self.center = 25
        if self.center >= 1175:
            self.center = 1175
        if self.moving_up:
            self.center2 -= 3
        if self.moving_down:
            self.center2 += 3
        if self.center2 <= 25:
            self.center2 = 25
        if self.center2 >= 545:
            self.center2 = 545
        """this makes the center of the ship the same as the new inputs that the user is doing"""
        self.rect.centerx = self.center
        self.rect.centery = self.center2

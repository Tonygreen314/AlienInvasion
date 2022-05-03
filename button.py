import pygame.font
import pygame


class Button:
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
        self.width = 200
        self.height = 50
        self.button_color = (100, 255, 0)
        self.text_color = (0, 100, 200)
        self.font = pygame.font.SysFont("Times New Roman", 48)
        self.rect = pygame.Rect(self.centerx-100, self.centery-25, self.width, self.height)
        self.rect_center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect_center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

import pygame
from settings import Settings
from ship import Ship
import Game_Functions as Gf
from pygame.sprite import Group
from button import Button
"""
Zachary Carroll
importing pygame,settings,the ship, the game functions, 
and group in the section of pygame.sprite into the code
define main game function
"""


def alien_invasion():
    pygame.init()
    settings = Settings()
    """creates the display of the game"""
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    """declares what the window  name is"""
    pygame.display.set_caption('Alien Invasion')

    """makes a play button"""
    play_button = Button(screen, "Start Game")

    """add ship"""
    ship = Ship(screen, 0)

    """make a group to store bullets, aliens, and the boss in"""
    bullets = Group()
    aliens = Group()
    boss = Group()

    """creates the fleet of aliens"""
    Gf.create_fleet(settings, screen, ship, aliens, boss)

    """loop to start animation"""
    while settings.game_on:

        """checks if the user has hit any of the keys"""
        Gf.check_events(settings, screen, ship, bullets, play_button)
        """updates the screen with a bullet when space bar is pressed"""
        bullets.update()
        Gf.limit_bullets(bullets)
        """updates the screen to show any of the new inputs"""
        Gf.update_screen(screen, settings, ship, bullets, aliens, boss, play_button)


"""runs the game"""
alien_invasion()

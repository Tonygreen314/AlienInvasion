import pygame
import sys
from aliens import Alien
from bullets import Bullets
from Mother_Alien import Boss


def check_events(settings, screen, ship, bullets):
    """this function check for key and mouse and checks for movement"""
    """creates a way to exit the game"""
    for event in pygame.event.get():
        """quits the game"""
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down_events(ship, event, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            key_up_events(event, ship)


"""checks the code to see if the user is not pressing the button"""


def key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


"""checks when if the key is pressed down and then moves the ship 
corresponding to the input that is given"""


def key_down_events(ship, event, settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullets(settings, screen, ship)
        if len(bullets) < settings.bullet_limit:
            bullets.add(new_bullet)


def update_screen(screen, settings, ship, bullets, aliens, boss):
    """adds the color to the screen"""
    screen.fill(settings.bg_color)
    """update the ship"""
    ship.update()

    """draws the ship and the alien """
    ship.blitme()

    """draw bullets on the screen"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)
    boss.draw(screen)
    print_points(settings, screen)
    print_waves(settings, screen)
    """update the display"""
    pygame.display.flip()


def create_fleet(settings, screen, ship, aliens, boss):
    """create a fleet from aliens"""
    alien = Alien(settings, screen)
    number_of_aliens_x = get_number_of_aliens_x(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)
    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number, boss)


def get_number_of_aliens_x(settings, alien_width):
    """determine the number of aliens that fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    amount_of_aliens = int(available_space_x/(2 * alien_width))
    return amount_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y/(5*alien_height))
    return number_of_rows


def number_of_aliens(settings, alien_height, alien_width, ship_height):
    number_of_actual_aliens = get_number_rows(settings, alien_height, ship_height) \
                              * get_number_of_aliens_x(settings, alien_width)
    return number_of_actual_aliens


def create_alien(settings, screen, aliens, alien_number, row_number, big_boss):
    """create an alien and place it on a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = float(2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    boss = Boss(settings, screen)
    big_boss.add(boss)


def check_collision(bullets, aliens, boss, settings):
    alien_collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    boss_collision = pygame.sprite.groupcollide(bullets, boss, True, True)

    if alien_collision:
        settings.points += 1

    if boss_collision:
        settings.points += 10


def limit_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.top < 20:
            bullets.remove(bullet)


def print_points(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Number of Points: " + str(settings.points), True, (0, 255, 0))
    screen.blit(surface, (920, 570))


def print_waves(settings, screen):
    waves = settings.alien_speed
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Number of Waves: "+str(waves), True, (0, 255, 0))
    screen.blit(surface, (15, 570))


def restart(settings, screen, ship, aliens, boss):
    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens, boss)
        settings.alien_speed += 1

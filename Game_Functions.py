import pygame
import sys
from Images.aliens import Alien
from bullets import Bullets
from Mother_Alien import Boss
from time import sleep


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
    image = pygame.image.load("Images/Space-invader-background-final.png")
    screen.blit(image, (0, 0))

    """update the ship"""
    ship.blitme()
    ship.update()

    """draw bullets on the screen"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    update_aliens(settings, screen, ship, aliens, bullets, boss)
    aliens.draw(screen)
    boss.draw(screen)
    print_points(settings, screen)
    print_waves(settings, screen)
    print_lives(settings, screen)
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


def update_fleet(aliens):
    for alien in aliens:
        alien.direction = alien.direction * -1
        alien.rect.y += alien.drop_speed


def update_aliens(settings, screen, ship, aliens, bullets, boss):
    # draw fleet of aliens
    aliens.draw(screen)
    aliens.update()

    for alien in aliens:
        if alien.check_screen():
            update_fleet(aliens)
            break
    check_collision(bullets, aliens, boss, settings, ship, screen)

    new_wave(settings, screen, ship, aliens, boss)


def check_collision(bullets, aliens, boss, settings, ship, screen):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        settings.score += int(settings.points)
    boss_hit = pygame.sprite.groupcollide(bullets, boss, True, True)
    if boss_hit:
        settings.score += 50
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, ship, aliens, bullets, boss)

    alien_invasion(settings, screen, ship, aliens, bullets, boss)


def limit_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.top < 0:
            bullets.remove(bullet)


def print_points(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Number of Points: " + str(settings.score), True, (200, 255, 0))
    screen.blit(surface, (880, 570))


def print_waves(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Number of Waves: "+str(settings.wave_number), True, (200, 255, 0))
    screen.blit(surface, (15, 570))


def new_wave(settings, screen, ship, aliens, boss):
    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens, boss)
        settings.alien_speed += 1


def print_lives(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Number of Lives: " + str(settings.lives), True, (200, 255, 0))
    screen.blit(surface, (470, 570))


def end_game(screen, ship, aliens):
    font = pygame.font.SysFont("Times New Roman", 50, True, False)
    surface = font.render("You Loose", True, (200, 255, 0))
    screen.blit(surface, (515, 300))
    ship.speed = 0
    aliens.speed = 0


def reset_wave(settings, screen, ship, aliens, bullets, boss):
    aliens.empty()
    bullets.empty()
    boss.empty()
    ship.center_ship()
    sleep(.5)
    create_fleet(settings, screen, ship, aliens, boss)


def ship_hit(settings, screen, ship, aliens, bullets, boss):
    settings.lives -= 1
    if settings.lives > 0:
        reset_wave(settings, screen, ship, aliens, bullets, boss)
    else:
        end_game(screen, ship, settings)
        settings.lives = 0
        ship.center_ship()


def alien_invasion(settings, screen, ship, aliens, bullets, boss):
    for alien in aliens:
        if alien.rect.bottom > settings.screen_height:
            settings.score -= int(settings.points*len(aliens)/2)
            reset_wave(settings, screen, ship, aliens, bullets, boss)
            break


def increase_difficulty(settings):
    settings.wave_number += 1
    settings.alien_speed *= settings.difficulty_scale
    settings.alien_drop_speed += 1 * settings.difficulty_scale
    settings.points *= settings.difficulty_scale
    settings.scale *= 0.96

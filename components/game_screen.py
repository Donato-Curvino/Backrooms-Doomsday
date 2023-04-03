import pygame
import components.button as button
import os


def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def start_screen(screen):
    # load button images
    start_img = pygame.image.load("assets/button_start.png").convert_alpha()
    quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
    monster = pygame.image.load("assets/monster.png")
    monster = pygame.transform.scale(monster, (800, 600))

    # create button instances
    start_button = button.Button(20, 200, start_img, 1)  # 308
    quit_button = button.Button(20, 400, quit_img, 1)  # 310

    screen.blit(monster, (0, 0))
    if start_button.draw(screen):
        print("resume button pressed")
        return 1
    if quit_button.draw(screen):
        print("quit button pressed")
        return 4
    draw_text(screen, "Backrooms", pygame.font.SysFont("arialblack", 60), (255, 255, 0), 20, 10)
    draw_text(screen, "Doomsday", pygame.font.SysFont("arialblack", 60), (255, 255, 0), 20, 80)


def main_game(screen, player, key):
    pygame.draw.rect(screen, (255, 0, 0), player)
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_k] == True:
        return 2


def end_screen(screen):
    again_img = pygame.image.load("assets/button_again.png").convert_alpha()
    quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()

    # create button instances
    again_button = button.Button(246, 200, again_img, 1)  # 308
    quit_button = button.Button(247, 400, quit_img, 1)  # 310

    # again_button = button.Button(, 200, again_img, 1)

    if again_button.draw(screen):
        return 1
    if quit_button.draw(screen):
        return 4
    draw_text(screen, "You Died", pygame.font.SysFont("arialblack", 80), (255, 255, 0), 200, 20)

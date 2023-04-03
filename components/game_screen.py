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

    screen.fill((230, 230, 230))
    screen.blit(monster, (400, 80))
    if start_button.draw(screen):
        return 1
    if quit_button.draw(screen):
        return 4
    draw_text(screen, "Backrooms", pygame.font.SysFont("arialblack", 60), (255, 255, 0), 20, 10)
    draw_text(screen, "Doomsday", pygame.font.SysFont("arialblack", 60), (255, 255, 0), 20, 80)


def main_game(screen, p, m, clk, DEBUG, dt):
    screen.fill((230, 230, 155))

    p.move(dt)
    m.draw(DEBUG)
    p.draw(DEBUG)
    # enemy.draw()

    dt = clk.tick(60)
    # print(dt)
    pygame.display.flip()
    # print(p.angle)
    if p.win():
        state = 4
        print("You win!!")


def end_screen(screen):
    again_img = pygame.image.load("assets/button_again.png").convert_alpha()
    quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
    monster = pygame.image.load("assets/monster.png")
    monster = pygame.transform.scale(monster, (800, 600))

    # create button instances
    again_button = button.Button(20, 200, again_img, 1)  # 308
    quit_button = button.Button(20, 400, quit_img, 1)  # 310

    # again_button = button.Button(, 200, again_img, 1)

    screen.fill((230, 230, 230))
    screen.blit(monster, (400, 80))
    if again_button.draw(screen):
        return 1
    if quit_button.draw(screen):
        return 4
    draw_text(screen, "You Found the Exit!", pygame.font.SysFont("arialblack", 80), (255, 255, 0), 20, 10)

import pygame
from multiprocessing import Pool
import components.game_screen
from components.player import *
from components.map import *
from components.constants import *
from components.sprite_object import *

if __name__ == "__main__":
    pygame.init()

    # Note: can change to 1920, by 1080 for completion
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode(RES)

    player = pygame.Rect((300, 250, 50, 50))

    #game variables
    game_start = False
    menu_state = "main"

    # #define fonts
    # font = pygame.font.SysFont("arialblack", 40)

    # #define colours
    # TEXT_COL = (255, 255, 255)

    # #load button images
    # resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    # quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    # back_img = pygame.image.load('images/button_back.png').convert_alpha()

    # create button instances
    # resume_button = button.Button(304, 125, resume_img, 1)
    # quit_button = button.Button(336, 375, quit_img, 1)
    # back_button = button.Button(332, 450, back_img, 1)

    gs = components.game_screen
    state = 0
    m = Map(screen)
    p_img = pygame.image.load("assets/arrow.png").convert_alpha()
    p = Player(m, p_img)
    clk = pygame.time.Clock()
    enemy = Enemy(screen, p, m)
    dt = 1

    pool = Pool()

    run = True
    while run:
        screen.fill((0, 0, 0))
        key = pygame.key.get_pressed()

        # check if game is paused
        if state == 0 and gs.start_screen(screen):
            state = gs.start_screen(screen)
        # elif state == 1 and gs.main_game(screen, player, key):
        #     state = gs.main_game(screen, player, key)
        elif state == 1:
            screen.fill((230, 230, 155))

            p.move(dt)
            m.draw(DEBUG)
            # p.draw(screen, pool.map(p.raytrace, ANGLES), p_img)
            # rays = pool.map(p.raytrace, ANGLES)
            # pygame.surfarray.pixels2d(screen)[:] = pool.map(p.render_line, rays)
            pygame.surfarray.pixels2d(screen)[:] = pool.map(p.draw_line, ANGLES)
            enemy.draw()

            dt = clk.tick(60)
            # print(dt)
            pygame.display.set_caption(f"{clk.get_fps():.1f}")
            pygame.display.flip()
            # print(p.angle)
            if p.win():
                state = 2
                print("You win!!")
        elif state == 2 and gs.end_screen(screen):
            state = gs.end_screen(screen)
        elif state == 4:
            run = False

        # game loop check for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT  or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True

        pygame.display.update()

    pygame.quit()

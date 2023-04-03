import pygame
import game_screen

pygame.init()

# Note: can change to 1920, by 1080 for completion
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

# #create button instances
# resume_button = button.Button(304, 125, resume_img, 1)
# quit_button = button.Button(336, 375, quit_img, 1)
# back_button = button.Button(332, 450, back_img, 1)
gs = game_screen
state = 0

run = True
while run:
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()

    #check if game is paused
    if state == 0 and gs.start_screen(screen):
        state = gs.start_screen(screen)
    elif state == 1 and gs.main_game(screen, player, key):
        state = gs.main_game(screen, player, key)
    elif state == 2 and gs.end_screen(screen):
        state = gs.end_screen(screen)
    elif state == 4:
        run = False
        

    # game loop check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = True

    pygame.display.update()

pygame.quit()

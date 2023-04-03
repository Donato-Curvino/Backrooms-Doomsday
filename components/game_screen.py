import pygame
import button

def set_images(screen):
	#load button images
	resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
	quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
	monster = pygame.image.load("images/monster.png")
	monster = pygame.transform.scale(monster, (800, 600))

	#create button instances
	resume_button = button.Button(304, 125, resume_img, 1)
	quit_button = button.Button(336, 375, quit_img, 1)

	return resume_button, quit_button, monster

def draw_text(screen, text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def start_screen(screen):
	
	resume_button, quit_button, monster = set_images(screen)

	screen.blit(monster, (0, 0))
	if resume_button.draw(screen):
		print("resume button pressed")
		return 1
	if quit_button.draw(screen):
		print("quit button pressed")
		return 4
	draw_text(screen, "Backrooms: Doomsday", pygame.font.SysFont("arialblack", 40), (255, 255, 255), 20, 10)


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
    elif key[pygame.K_l] == True:
	    return 4

def end_screen(screen):
	resume_button, quit_button, monster = set_images(screen)
	
	if resume_button.draw(screen):
		return 1
	if quit_button.draw(screen):
		return 4
	else:
		return 0
	draw_text(screen, "Backrooms: Doomsday", pygame.font.SysFont("arialblack", 40), (255, 255, 255), 20, 10)

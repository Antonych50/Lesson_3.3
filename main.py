import pygame
import random
import time

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/мишень.jpg")
target_image = pygame.image.load("img/apple1.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
#color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color = (255,255,255)
game_score = 0
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                game_score+= 10
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                game_score-= 10
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()
text_surface = font.render("У Вас " + str(game_score) + "очков!", True, (0, 0, 255))
screen.blit(text_surface, (100, 100))
time.sleep(25)
pygame.quit()
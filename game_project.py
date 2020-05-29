#from pygame import *
import pygame

pygame.init()

FPS = 60
BLACK = (0,0,0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((600, 800))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

square = pygame.rect.Rect(0, 0, 50, 50)
square.center = screen_rect.center

X_SPEED = 5
Y_SPEED = 5

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if square.right >= screen_rect.right:
        X_SPEED = -5
    if square.left <= screen_rect.left:
        X_SPEED = 5
    if square.top <= screen_rect.top:
        Y_SPEED = 5
    if square.bottom >= screen_rect.bottom:
        Y_SPEED = -5
    
    square.x += X_SPEED
    square.y += Y_SPEED
    
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, square)
    
    pygame.display.flip()

pygame.quit()
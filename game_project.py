#from pygame import *
import pygame

pygame.init()

BLACK = (0,0,0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

square = pygame.rect.Rect(0, 0, 50, 50)

running = True
while running:
    pygame.event.get()
    clock.tick(1)
    square.x += 5
    square.y += 5
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, square)
    pygame.display.flip()

pygame.quit()
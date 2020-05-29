import pygame

pygame.init()

RED = (255, 0, 0)

screen = pygame.display.set_mode((600, 800))

square = pygame.rect.Rect(0, 0, 50, 50)

running = True
while running:
    square.x += 5
    square.y += 5
    pygame.draw.rect(screen, RED, square)
    pygame.display.flip()

pygame.quit()
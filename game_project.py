#from pygame import *
import pygame

pygame.init()

# constants
FPS = 60
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# screen and clock setup
screen = pygame.display.set_mode((600, 800))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

# ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.x_speed = 5
        self.y_speed = 5
        
    def update(self):
        if self.rect.right >= screen_rect.right:
            self.x_speed = -5
        if self.rect.left <= screen_rect.left:
            self.x_speed = 5
        if self.rect.top <= screen_rect.top:
            self.y_speed = 5
        if self.rect.bottom >= screen_rect.bottom:
            self.y_speed = -5
    
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

# paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,15))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.rect.bottom = screen_rect.bottom -10

all_sprites = pygame.sprite.Group()

ball = Ball()
all_sprites.add(ball)

paddle = Paddle()
all_sprites.add(paddle)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
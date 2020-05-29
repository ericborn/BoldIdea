#from pygame import *
import pygame

pygame.init()

# constants
FPS = 60
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRICKS_PER_ROW = 10
NUM_ROWS = 5

# screen and clock setup
screen = pygame.display.set_mode((600, 800))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

# ball sprite class
# sets size, color, starting position and speed
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_image = pygame.image.load('ball.png').convert_alpha()
        self.image = pygame.transform.scale(ball_image, (20, 20))
        self.rect = self.image.get_rect()
        self.reset()
 
    def reset(self):
        self.rect.center = screen_rect.center
        self.x_speed = 5
        self.y_speed = 5
        self.lost = False

    # prevents the ball from bouncing off the screen   
    def update(self):
        if self.rect.right >= screen_rect.right:
            self.x_speed = -5
        if self.rect.left <= screen_rect.left:
            self.x_speed = 5
        if self.rect.top <= screen_rect.top:
            self.y_speed = 5
        if self.rect.bottom >= screen_rect.bottom:
            self.lost = True

    # updates speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

# paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()      
        paddle_image = pygame.image.load('paddle.png').convert_alpha()
        self.image = pygame.transform.scale(paddle_image, (100, 20))
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.rect.bottom = screen_rect.bottom -10
        
    def update(self):
        keys = pygame.key.get_pressed()
        # allows paddle to be moved with left and right arrow keys
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        # prevents paddle from leaving screen
        if self.rect.right >= screen_rect.right:
            self.rect.right = screen_rect.right
        if self.rect.left <= screen_rect.left:
            self.rect.left = screen_rect.left

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        brick_image = pygame.image.load('blue_brick.png').convert_alpha()
        self.image = brick_image
        self.rect = self.image.get_rect()

# creates a group for all sprites
all_sprites = pygame.sprite.Group()

# instantiate the ball class, add ball to sprite group
ball = Ball()
all_sprites.add(ball)

# instantiate the paddle class, add paddle to sprite group
paddle = Paddle()
all_sprites.add(paddle)

# while loop that runs the game
running = True
while running:
    # sets the clock tick rate to our FPS constant
    clock.tick(FPS)

    # allows the game to be closed and quit the program on clicking the X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # updates the sprites group on each tick kof the game
    all_sprites.update()
    
    if pygame.sprite.collide_rect(ball, paddle):
        ball.y_speed = -5
        
    if ball.lost:
        ball.reset()
    
    # fills the background with black
    screen.fill(BLACK)
    
    # draws the sprites on screen
    all_sprites.draw(screen)
    
    #flips the display
    pygame.display.flip()

pygame.quit()
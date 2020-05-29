#from pygame import *
import pygame

pygame.init()

# constants
FPS = 60

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#bricks
BRICKS_PER_ROW = 10
NUM_ROWS = 5
BLANK_ROWS = 2

# game stats
score = 0
lives = 3
game_over = False

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
    def __init__(self, row, col):
        super().__init__()
        brick_image = pygame.image.load('blue_brick.png').convert_alpha()
        
        # calculate new size based on BRICKS_PER_ROW
        brick_width = round(screen_rect.width / BRICKS_PER_ROW)
        orig_size = brick_image.get_rect()
        scale_factor = (brick_width / orig_size.width)
        brick_height = round(orig_size.height * scale_factor)
        new_size = (brick_width, brick_height)
 
        
        # scale the image
        self.image = pygame.transform.scale(brick_image, new_size)
        self.rect = self.image.get_rect()
        
        # position the bricks
        row += BLANK_ROWS
        self.rect.x = col * brick_width
        self.rect.y = row * brick_height

# creates a group for all sprites
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# instantiate the ball class, add ball to sprite group
ball = Ball()
all_sprites.add(ball)

# instantiate the paddle class, add paddle to sprite group
paddle = Paddle()
all_sprites.add(paddle)

# instantiate the brick class, add brick to sprite group
for row in range(0, NUM_ROWS):
    for col in range(0, BRICKS_PER_ROW):
        brick = Brick(row,col)
        all_sprites.add(brick)
        bricks.add(brick)
        
def draw_text(surface, text, pos=(0,0), color=WHITE, font_size=20, anchor='topleft'):
    arial = pygame.font.match_font('arial')
    font = pygame.font.Font(arial, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    setattr(text_rect, anchor, pos)
    surface.blit(text_surface, text_rect)

# while loop that runs the game
running = True
while running:
    # sets the clock tick rate to our FPS constant
    clock.tick(FPS)

    # allows the game to be closed and quit the program on clicking the X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if game_over:
        screen.fill(BLACK)
        draw_text(screen, "GAME OVER", screen_rect.center, font_size=80, anchor="center")
    
    # updates the sprites group on each tick of the game
    else:
        all_sprites.update()    
    
        # bounce ball if it hits paddle
        if pygame.sprite.collide_rect(ball, paddle):
            ball.y_speed = -5
        
        # reset ball if it passes below the bottom of screen
        if ball.lost:
            lives -= 1
            if lives == 0:
                game_over = True
            ball.reset()
        
        # check for ball hitting bricks, bounce down if it did
        collide_brick = pygame.sprite.spritecollideany(ball, bricks)
        if collide_brick:
            score += 1
            collide_brick.kill()
            ball.y_speed *= -1
        
        # fills the background with black
        screen.fill(BLACK)
        
        # draws the sprites on screen
        all_sprites.draw(screen)
        
        score_text = f"Score: {score} / Lives: {lives}"
        draw_text(screen, score_text, (8, 8))
        
        #flips the display
    pygame.display.flip()

pygame.quit()
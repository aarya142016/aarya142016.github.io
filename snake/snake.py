import pygame
import random

# Initialize pygame
pygame.init()
font = pygame.font.SysFont(None, 36)

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Snake settings
SQUARE_SIZE = 50
snake = [(400, 300)]  # start with one square
dx = 0
dy = 0

# Food settings
food_x = random.randrange(0, SCREEN_WIDTH, SQUARE_SIZE)
food_y = random.randrange(0, SCREEN_HEIGHT, SQUARE_SIZE)

score = 0
clock = pygame.time.Clock()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -SQUARE_SIZE
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = SQUARE_SIZE
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -SQUARE_SIZE
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = SQUARE_SIZE
                
    # Move snake: add new head
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # Wall collision → game over
    if (
    new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
    new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT
    ):
        running = False

    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == (food_x, food_y):
        score += 1
        food_x = random.randrange(0, SCREEN_WIDTH, SQUARE_SIZE)
        food_y = random.randrange(0, SCREEN_HEIGHT, SQUARE_SIZE)
    else:
        snake.pop()  # remove tail

    # Self-collision (ONLY after moving)
    if new_head in snake[1:]:
        running = False
      
    # Drawing
    screen.fill(WHITE)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    for part in snake:
        pygame.draw.rect(screen, BLUE, (part[0], part[1], SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.flip()

    clock.tick(10)  # move snake slower for grid-style movement

pygame.quit()
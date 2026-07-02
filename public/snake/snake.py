import pygame
import random
import asyncio
import sys

# Initialize pygame
pygame.init()

# Fonts
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game ")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
SQUARE_SIZE = 50

# Function to reset the game
def reset_game():
    global snake, dx, dy, food_x, food_y, score, game_over
    snake = [(400, 300)]
    dx, dy = 0, 0  # snake stays still until a key is pressed
    food_x = random.randrange(0, SCREEN_WIDTH, SQUARE_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT, SQUARE_SIZE)
    score = 0
    game_over = False

reset_game()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement keys
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -SQUARE_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = SQUARE_SIZE, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -SQUARE_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, SQUARE_SIZE

        # Restart key
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

    # Move the snake if game not over AND direction is set
    if not game_over and (dx != 0 or dy != 0):
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            game_over = True

        snake.insert(0, new_head)

        # Self collision
        if new_head in snake[1:]:
            game_over = True

        # Check if food eaten
        if new_head == (food_x, food_y):
            score += 1
            food_x = random.randrange(0, SCREEN_WIDTH, SQUARE_SIZE)
            food_y = random.randrange(0, SCREEN_HEIGHT, SQUARE_SIZE)
        else:
            snake.pop()  # remove tail

    # Draw snake and food
    for part in snake:
        pygame.draw.rect(screen, BLUE, (part[0], part[1], SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw game over
    if game_over:
        over_text = big_font.render("GAME OVER", True, RED)
        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(over_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 - 50))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 30))

    pygame.display.flip()
    await asyncio.sleep(1 / 10)
    
pygame.quit()

    

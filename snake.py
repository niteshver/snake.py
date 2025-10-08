import pygame
import random

pygame.init()

# -------- Window setup --------
screen_width = 500
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🐍 SnakeX")

# -------- Colors --------
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_green = (0, 100, 0)
bright_yellow = (255, 255, 0)

# -------- Background image --------
background_image = pygame.image.load(
    "/Users/niteshv1520/Documents/Python_Data_2025/Testing_Project_2025/snake.py/snake_background.jpg"
)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# -------- Font setup --------
font = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(gamewindow, color, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)

# -------- Main Game Function --------
def gameloop():
    # Snake starting position
    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0

    # Food position
    food_x = random.randint(20, screen_width - 40)
    food_y = random.randint(20, screen_height - 40)

    score = 0
    snk_list = []
    snk_length = 1
    fps = 50
    clock = pygame.time.Clock()
    game_over = False

    while True:
        if game_over:
            gamewindow.blit(background_image, (0, 0))
            text_screen("Game Over!", red, screen_width // 2 - 100, screen_height // 2 - 80)
            text_screen(f"Score: {score * 10}", red, screen_width // 2 - 80, screen_height // 2 - 30)
            text_screen("Press ENTER to Restart", white, screen_width // 2 - 150, screen_height // 2 + 40)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()  # Restart game

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    elif event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Snake eats food
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 1
                snk_length += 1
                food_x = random.randint(20, screen_width - 40)
                food_y = random.randint(20, screen_height - 40)

            # Background and Score
            gamewindow.blit(background_image, (0, 0))
            text_screen("Score: " + str(score * 10), red, 10, 10)

            # Update snake body
            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Game over conditions
            if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
                game_over = True

            if head in snk_list[:-1]:
                game_over = True

            # Draw food and snake
            pygame.draw.circle(gamewindow, bright_yellow, (food_x + snake_size // 2, food_y + snake_size // 2), snake_size // 2)
            plot_snake(gamewindow, dark_green, snk_list, snake_size)

            pygame.display.update()
            clock.tick(fps)

# -------- Run Game --------
gameloop()
pygame.quit()
quit()

import pygame
import random
import time

pygame.init()


snake_block = 30
width = 780
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")


snake_speed = 10


apple_img = pygame.image.load('apple.png')
apple_img = pygame.transform.scale(apple_img, (snake_block, snake_block))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (40, 40, 40)
BLUE = (100, 149, 237)


def draw_grid():
    for x in range(0, width, snake_block):
        pygame.draw.line(window, GRAY, (x, 0), (x, height))
    for y in range(0, height, snake_block):
        pygame.draw.line(window, GRAY, (0, y), (width, y))


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block-1, snake_block-1])

def game_loop():
    game_over = False
    game_close = False

    x1 = round(width/2/snake_block) * snake_block
    y1 = round(height/2/snake_block) * snake_block

    x1_change = 0
    y1_change = 0

    snake_list = []
    len_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    clock = pygame.time.Clock()

    apples_eaten = 0  # Счетчик съеденных яблок

    while not game_over:
        while game_close:
            window.fill(BLUE)
            font = pygame.font.SysFont(None, 50)
            text = font.render("Игра окончена! Q - выход, C - повтор", True, WHITE)
            window.blit(text, [width/6, height/3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0


        x1 += x1_change
        y1 += y1_change


        if x1 >= width:
            x1 = 0
        elif x1 < 0:
            x1 = width - snake_block
        if y1 >= height:
            y1 = 0
        elif y1 < 0:
            y1 = height - snake_block

        window.fill(BLUE)
        draw_grid()
        window.blit(apple_img, (foodx, foody))

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            apples_eaten += 1  
            if apples_eaten >= 10:
                print("Вы съели 10 яблок! Игра окончена.")
                game_over = True
            else:
                while True:
                    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
                    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
                    if [foodx, foody] not in snake_list:
                        break
                len_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

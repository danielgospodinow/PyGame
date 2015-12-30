import pygame
import random

pygame.init()

white = [255, 255, 255]
black = [0, 0, 0]
green = [0, 155, 0]
red = [255, 0, 0]

snake_head_image = pygame.image.load("snakehead01.png")
apple_image = pygame.image.load("apple_sprite_01.png")
snake_tail_image = pygame.image.load("snake_tail_01.png")
game_icon = pygame.image.load("danchoIcon.jpg")

pygame.display.set_icon(game_icon)

display_width = 800
display_height = 600

direction = "up"

fps = 10

gameDisplay = pygame.display.set_mode((display_width, display_height))  # Deklarirane na promenliwa koqto dyrji ekrana na igrata
pygame.display.set_caption("Snake- Dancho's first game.")  # Slaga title na .exe-to

python_clock = pygame.time.Clock()  # Promenliwa za kontrol na fps

small_font = pygame.font.SysFont("comicsansms", 25)
normal_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 100)


def snake(snake_size, snake_list):

    if direction == "up":
        head = pygame.transform.rotate(snake_head_image, 0)
    elif direction == "down":
        head = pygame.transform.rotate(snake_head_image, 180)
    elif direction == "right":
        head = pygame.transform.rotate(snake_head_image, 270)
    elif direction == "left":
        head = pygame.transform.rotate(snake_head_image, 90)

    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))

    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, green,
                         [XnY[0], XnY[1], snake_size, snake_size])  # Nachin 1 za chertane na prawoygylnik


def text_objects(text, color, font_size):
    if font_size == "small":
        text_surface = small_font.render(text, True, color)
    elif font_size == "normal":
        text_surface = normal_font.render(text, True, color)
    elif font_size == "large":
        text_surface = large_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(message, color, y_dispose=0, font_size="small"):
    text_surface, text_rect = text_objects(message, color, font_size)
    text_rect.center = (display_width/2), (display_height/2) + y_dispose
    gameDisplay.blit(text_surface, text_rect)


def score(score):
    score_text = small_font.render("Score: " + str(score), True, black)
    gameDisplay.blit(score_text, [0, 0])


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Dancho's first", black, font_size="normal", y_dispose=-115)
        message_to_screen("PYTHON", red, font_size="large", y_dispose=-40)
        message_to_screen("game!", black, font_size="normal", y_dispose=20)
        message_to_screen("Press C to play or Q to quit!", green, font_size="small", y_dispose=180)
        pygame.display.update()


def game_loop():
    game_exit = False
    game_over = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    snake_size = 15
    lead_x_change = 0
    lead_y_change = -10
    rand_big_apple_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    rand_big_apple_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
    big_apple_size = 20
    snake_list = []
    snake_lenght = 1
    global direction
    snake_turn_points = []
    game_score = 0

    while not game_exit:

        while game_over is True:
            gameDisplay.fill(white)
            message_to_screen("Game over!", red, y_dispose=-90, font_size="normal")
            message_to_screen("Press 'C' to play again or 'Q' to quit.", black, y_dispose=30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():  # Tozi for loop uprawlqwa eventite
            if event.type == pygame.QUIT:
                game_exit = True
            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = "left"
                    snake_turn_point = [[lead_x, lead_y], "left"]
                    snake_turn_points.append(snake_turn_point)
                    lead_x_change = -snake_size
                    lead_y_change = 0
                if event.key == pygame.K_d:
                    direction = "right"
                    snake_turn_point = [[lead_x, lead_y], "right"]
                    snake_turn_points.append(snake_turn_point)
                    lead_x_change = snake_size
                    lead_y_change = 0
                if event.key == pygame.K_w:
                    direction = "up"
                    snake_turn_point = [[lead_x, lead_y], "up"]
                    snake_turn_points.append(snake_turn_point)
                    lead_y_change = -snake_size
                    lead_x_change = 0
                if event.key == pygame.K_s:
                    direction = "down"
                    snake_turn_point = [[lead_x, lead_y], "down"]
                    snake_turn_points.append(snake_turn_point)
                    lead_y_change = snake_size
                    lead_x_change = 0

        if lead_x >= display_width - snake_size or lead_x < 0 or lead_y >= display_height - snake_size or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_lenght:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment[0] == snake_head[0] and each_segment[1] == snake_head[1]:
                game_over = True

        gameDisplay.fill(white)  # Slaga celiq background-color da e white
        # pygame.draw.rect(gameDisplay, red, [rand_big_apple_x, rand_big_apple_y, big_apple_size, big_apple_size])
        gameDisplay.blit(apple_image, (rand_big_apple_x, rand_big_apple_y))
        snake(snake_size, snake_list)
        # gameDisplay.fill(red, rect=[200, 200, 50, 50])  # Nachin 2 za chertane na prawoygylnik
        '''if len(snake_turn_points) > 1 and snake_turn_points[-1][0][0] == snake_list[0][0]:
            print("tail should now rotate!")
            print(snake_turn_points[0][0][0], " ", snake_turn_points[0][0][1])
            if snake_turn_points[-1][1] == "up":
                print("up")
                pygame.transform.rotate(snake_tail_image, 0)
            if snake_turn_points[-1][1] == "down":
                print("down")
                pygame.transform.rotate(snake_tail_image, 180)
            if snake_turn_points[-1][1] == "right":
                print("right")
                pygame.transform.rotate(snake_tail_image, 270)
            if snake_turn_points[-1][1] == "left":
                print("left")
                pygame.transform.rotate(snake_tail_image, 90)
            snake_turn_points.remove(snake_turn_points[-1])'''
        if len(snake_list) > 1:
            gameDisplay.blit(snake_tail_image, (snake_list[0][0], snake_list[0][1]))
        score(game_score)
        pygame.display.update()  # Risuwa wsichko koeto wsichko e definirano nad tozi update() metod

        if (lead_x > rand_big_apple_x and lead_x < rand_big_apple_x + big_apple_size) or (lead_x + snake_size > rand_big_apple_x and lead_x + snake_size < rand_big_apple_x + big_apple_size):
            if (lead_y > rand_big_apple_y and lead_y < rand_big_apple_y + big_apple_size) or (lead_y + snake_size > rand_big_apple_y and lead_y + snake_size < rand_big_apple_y + big_apple_size):
                snake_lenght += 6
                game_score += 1
                rand_big_apple_x = random.randrange(0, display_width - big_apple_size)
                rand_big_apple_y = random.randrange(0, display_height - big_apple_size)

        python_clock.tick(fps)  # Prawim igrata da wyrwi s 10fps- po princip 30 fps e nai polzwanoto fps

    pygame.quit()
    quit()

game_intro()
game_loop()


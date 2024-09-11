import pygame, random, math, sys, os

pygame.init()

resolution = (500, 500)

window = pygame.display.set_mode(resolution)

pygame.display.set_caption("PySnake")

icon_ico_path = os.path.join("pictures", "icon.ico")
icon_png_path = os.path.join("pictures", "icon.png")
try:
    icon = pygame.image.load(icon_ico_path)
    pygame.display.set_icon(icon)
except Exception as e1:
    print(f"Error loading icon.ico: {e1}\n")
    print("Attempting to load icon.png as a fallback.\n")
    try:
        icon = pygame.image.load(icon_png_path)
        pygame.display.set_icon(icon)
    except Exception as e2:
        print(f"Error loading icon.png: {e2}\n")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 255, 0)

width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]

framerate_speed = 50
eps = 0.9
air = 0.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
tick_speed = pygame.time.Clock()

# todo: the function update_high_score() (I FORGOT WHAT IT WAS SUPPOSED TO BE)
def update_high_score():
    pass

# todo: finish the function below
def high_scores():
    pass

def menu():
    font_style = pygame.font.SysFont("Arial", 20)
    text = font_style.render("--- Menu ---", True, white)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                start_menu()
            elif key[pygame.K_h]:
                high_scores()
            elif key[pygame.K_k]:
                keyboard_shortcuts()
        window.fill(black)
        text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
        window.blit(text, text_rect)
        pygame.display.update()

def start_menu():

    font_style = pygame.font.SysFont("Arial", 20)
    text = font_style.render("Press \"S\" to start", True, white)
    #text_width = text.get_width()
    #text_height = text.get_height()
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                game_loop()
            elif key[pygame.K_k]:
                keyboard_shortcuts()
        window.fill(black)
        text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
        window.blit(text, text_rect)
        pygame.display.update()

def keyboard_shortcuts():
    font_style = pygame.font.SysFont("Arial", 20)
    text = font_style.render("--- Keyboard Shortcuts ---", True, white)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_m]:
                menu()
            elif key[pygame.K_s]:
                game_loop()
        window.fill(black)
        text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
        window.blit(text, text_rect)
        pygame.display.update()
    pygame.quit()
    sys.exit()

high_score_path = "user_files/high_score"

def save_score(high_score):
    with open(high_score_path, 'r') as file:
        maximum = max(high_score, int(file.read(1)))
    with open(high_score_path, 'w') as file:
        file.write(str(maximum))

def reset_high_score():
    with open(high_score_path, 'w') as f:
        f.write('0')

def get_max_score():
    high_score_path = "user_files/high_score"
    with open(high_score_path, "r") as f:
        max_score = f.read()
        return max_score

def check_if_outside(x, y, snake_size):
    if y + snake_size > height:
        y = height - snake_size

    if y < 0:
        y = 0

    if x + snake_size > width:
        x = width - snake_size

    if x < -1:
        x = 0

    return [x, y]

def game_loop():

    boost_multiplier = 100  # multiplier for speed when the space bar is pressed
    boost_active = False
    boost_start_time = 0  # When the boost started

    x1 = width / 2
    y1 = height / 2
    snake_size = 15
    food_size = 35
    x_food = random.randrange(0, 500 - food_size)
    y_food = random.randrange(0, 500 - food_size)
    snake_list = []
    snake_length = 1
    x_speed = 0
    y_speed = 0
    max_speed = 3
    food_png_path = os.path.join("pictures", "food.png")
    food = pygame.image.load(food_png_path).convert_alpha()
    image_food = pygame.transform.scale(food, (food_size, food_size))
    snake_path = os.path.join("pictures", "snake.png")
    snake = pygame.image.load(snake_path).convert_alpha()
    image_snake = pygame.transform.scale(snake, (snake_size, snake_size))
    run = True
    while run:
        font_style = pygame.font.SysFont("Arial", 20)
        # text_time = 60
        window.fill(blue)
        score = font_style.render("Score:  " + str(snake_length - 1), True, white)
        window.blit(score, [10, 5])
        speed = font_style.render("Speed: " + str(round(math.sqrt(x_speed**2 + y_speed**2))), True, white)
        window.blit(speed, [10, 25])
        
        xy_format_path = "user_files/xy_format"
        with open(xy_format_path, "rt") as f:
            r = f.readline().strip()
            try:
                r = int(r)
            except ValueError:
                window.blit(font_style.render('Invalid coordinates formatting...', True, white), [260, 5])
            if r == 0:
                coords = font_style.render(f"XY: {x1:.0f} {y1:.0f}", True, white)
                window.blit(coords, [400, 5])
            elif r == 1:
                coords = font_style.render(f"XY: {x1:.1f} {y1:.1f}", True, white)
                window.blit(coords, [375, 5])
            elif r == 2:
                coords = font_style.render(f"XY: {x1:.2f} {y1:.2f}", True, white)
                window.blit(coords, [360, 5])
            elif r == 3:
                coords = font_style.render(f"XY: {x1:.3f} {y1:.3f}", True, white)
                window.blit(coords, [340, 5])
            else:
                window.blit(font_style.render('Invalid coordinates formatting...', True, white), [260, 5])

        max_score = font_style.render("High Score: " + get_max_score(), True, white)
        window.blit(max_score, [10, 45])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(snake_length - 1)
                run = False
                sys.exit()

            elif keys[pygame.K_r]:
                reset_high_score()

            elif keys[pygame.K_m]:
                menu()

            elif keys[pygame.K_n]:
                game_loop()

            elif keys[pygame.K_k]:
                keyboard_shortcuts()

            elif keys[pygame.K_t]:
                with open(high_score_path, 'w') as f:
                    current_score = snake_length - 1
                    f.write(str(current_score))

            elif keys[pygame.K_LEFT]:
                if x_speed > -max_speed:
                    x_speed -= 1

            elif not keys[pygame.K_LEFT]:
                x_speed *= air
                y_speed *= air

            elif keys[pygame.K_RIGHT]:
                if x_speed < max_speed:
                    x_speed += 1

            elif not keys[pygame.K_RIGHT]:
                x_speed *= air
                y_speed *= air

            elif keys[pygame.K_UP]:
                if y_speed > -max_speed:
                    y_speed -= 1

            elif not keys[pygame.K_UP]:
                x_speed *= air
                y_speed *= air

            elif keys[pygame.K_DOWN]:
                if y_speed < max_speed:
                    y_speed += 1

            elif not keys[pygame.K_DOWN]:
                x_speed *= air
                y_speed *= air

            if keys[pygame.K_SPACE] and not boost_active:
                boost_active = True
                boost_start_time = pygame.time.get_ticks()  # Record the time boost started
                x_speed *= boost_multiplier  # Apply speed boost

            # Check if boost duration is over
            if boost_active:
                current_time = pygame.time.get_ticks()
                if current_time - boost_start_time >= 100:  # 100 milliseconds = 0.1 seconds
                    x_speed /= boost_multiplier  # Revert speed back to normal
                    boost_active = False  # Disable boost again

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if x_speed > -max_speed:
                x_speed -= 1

        if not keys[pygame.K_LEFT]:
            x_speed *= air
            y_speed *= air

        if keys[pygame.K_RIGHT]:
            if x_speed < max_speed:
                x_speed += 1

        if not keys[pygame.K_RIGHT]:
            x_speed *= air
            y_speed *= air

        if keys[pygame.K_UP]:
            if y_speed > -max_speed:
                y_speed -= 1

        if not keys[pygame.K_UP]:
            x_speed *= air
            y_speed *= air

        if keys[pygame.K_DOWN]:
            if y_speed < max_speed:
                y_speed += 1

        if not keys[pygame.K_DOWN]:
            x_speed *= air
            y_speed *= air


        if x1 + snake_size >= pygame.display.get_window_size()[0] or x1 < 0:
            x_speed = - x_speed * eps

        if y1 + snake_size >= pygame.display.get_window_size()[1] or y1 < 0:
            y_speed = - y_speed * eps

        x1, y1 = check_if_outside(x1, y1, snake_size)
        x_speed *= air
        y_speed *= air
        x1 += x_speed
        y1 += y_speed

        snake_head = [x1, y1]
        head_center = [x1 + snake_size / 2, y1 + snake_size / 2]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del (snake_list[0])
        for i in snake_list:
#            with open("snake_skin_active", "rt"):
#                snake_skin_active_path = os.path.join("user_files", "snake_skin_active")
#                snake_skin_active = snake_skin_active_path
#                from user_files/snake_skin_active import snake_skin_active_bool
#                if snake_skin_active_bool == True:
            window.blit(image_snake, (i[0], i[1]))
#                else:
#                    with open("snake_color", "rt") as snake_color_file:
#                        pygame.draw.rect(window, white)
            window.blit(image_food, (x_food, y_food))
        if (head_center[0] - x_food - food_size/2) ** 2 + (head_center[1] - y_food - food_size/2) ** 2 <= (food_size / 2) ** 2:
            x_food = random.randrange(0, 500 - food_size)
            y_food = random.randrange(0, 500 - food_size)
            snake_length += 1
            eating_sound_path = os.path.join("sounds", "eating.mp3")
            eating_sound = pygame.mixer.Sound(eating_sound_path)
            eating_sound.play()
            
        tick_speed.tick(framerate_speed)

        pygame.display.update()
        
if __name__ == '__main__':
    start_menu()

pygame.quit()

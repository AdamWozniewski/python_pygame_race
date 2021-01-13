import time
import random
from parts.init import *
from parts.colors import *
from parts.images import *
from parts.sounds import *
from parts.variables import *


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))
        if click[0] == 1:
            return 1
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText, white)
    TextRect.center = ((x + w / 2), (y + h / 2))
    gameDisplay.blit(TextSurf, TextRect)


def things_dodged(count, high_score, thing_speed):
    font = pygame.font.SysFont(None, 25)
    score = font.render("Ominięte: " + str(count), True, red)
    highscore = font.render("Najlepszy wynik: " + str(high_score), True, red)
    speed = font.render("Prędkość: " + str(thing_speed) + "Km/h", True, red)
    gameDisplay.blit(score, (10, 0))
    gameDisplay.blit(highscore, (10, 27))
    gameDisplay.blit(speed, (display_width - 125, 0))


def high_score_update(dodged):
    hs = open('data/hight_score.txt', 'w')
    temp = str(dodged)
    hs.write(temp)


def things(thingx, thingy):
    gameDisplay.blit(obstacle_Img, (thingx, thingy))


def car(x, y, dir):
    if dir == 0:
        gameDisplay.blit(carImg, (x, y))
    if dir == -1:
        gameDisplay.blit(carLeft, (x, y))
    if dir == 1:
        gameDisplay.blit(carRight, (x, y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, shift_x, shift_y, color, sleep_time):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((display_width / 2 - shift_x), (display_height / 2 - shift_y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(sleep_time)


def title_msg(shift_x, shift_y, color):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects("Python race", largeText, color)
    TextRect.center = ((display_width / 2 - shift_x), (display_height / 3 - shift_y))
    gameDisplay.blit(TextSurf, TextRect)
    time.sleep(0.15)
    pygame.display.update()


def title():
    height_anim = display_height
    pygame.mixer.Sound.play(intro_1)
    while height_anim > -600:
        gameDisplay.fill(white)
        things(display_width / 2 - thing_width / 2, height_anim)
        height_anim -= 1.5
        pygame.display.update()
    title_msg(0, 0, black)
    time.sleep(0.1)
    pygame.mixer.Sound.play(intro_2)


def motion_texture(thing_starty):
    gameDisplay.blit(texture, (0, thing_starty - 400))
    gameDisplay.blit(texture, (0, thing_starty))
    gameDisplay.blit(texture, (0, thing_starty + 400))


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display("AUTO ROZBITE", 0, 0, red, 0)
    while True:
        play = button("Replay", button_start_x, new_game_y, button_width, button_height, blueLight, blue)
        quit_game = button("Koniec", button_start_x, quit_y, button_width, button_height, redLight, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quit_game == 1 or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if play == 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_play()
        pygame.display.update()
        clock.tick(15)


def game_start():
    intro = True
    gameDisplay.fill(white)
    title()
    quit_game = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quit_game == 1 or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
        play = button("Nowa gra", button_start_x, new_game_y, button_width, button_height, blueLight, blue)
        quit_game = button("Koniec", button_start_x, quit_y, button_width, button_height, redLight, red)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_game = 1
        if play or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            intro = False

        pygame.display.update()
        clock.tick(15)


def counter_321():
    count = 1
    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(ignition)
    while count >= 0:
        gameDisplay.blit(background, backgroundRect)
        car(display_width * 0.40, display_height * 0.6, 0)
        if count == 0:
            message_display("START!", 0, 0, green, 0.75)
            pygame.mixer.music.play(-1)
        else:
            message_display(str(count), 0, 0, red, 0.75)
        count -= 1
    clock.tick(15)


def pause():
    pygame.mixer.music.pause()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            message_display("pauza", 0, 0, blue, 1.5)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.unpause()
                    return
        pygame.display.update()
        clock.tick(15)


def game_play():
    pygame.mixer.music.play(-1)
    x = (display_width * 0.4)
    y = (display_height * 0.6)
    x_change = 0

    thing_startx = random.randrange(8, display_width - thing_width - 8)
    thing_starty = -600
    thing_speed = 5

    dodged = 0
    dir = 0

    high_score_file = open('data/hight_score.txt', 'r')
    high_score = high_score_file.read()

    gameExit = False

    counter_321()

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -10
                    dir = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 10
                    dir = 1
                if event.key == pygame.K_SPACE:
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    dir = 0
        x += x_change
        gameDisplay.blit(background, backgroundRect)

        motion_texture(thing_starty)

        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        car(x, y, dir)

        things_dodged(dodged, high_score, thing_speed)
        # definiujemy kolizje
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
        if dodged > int(high_score):
            high_score_update(dodged)

        if y < thing_starty + thing_height - 15 and x > thing_startx - car_width - 5 and x < thing_startx + thing_width - 5:
            crash()

        pygame.display.update()
        clock.tick(60)

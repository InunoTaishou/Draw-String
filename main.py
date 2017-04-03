import pygame as Game
import datetime as date_time
import getpass
import os
import sys
import math
import Graphics

# window will start at 0, 0
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
time_regex = '%I:%M %p\n%A, %h %d'
username = getpass.getuser()

Game.init()

display_info = Game.display.Info()
time_game = Game.time.Clock()

# string formats for each text to draw
format_time = Graphics.StringFormat(Graphics.ALIGNMENT_CENTER, Graphics.ALIGNMENT_CENTER)
format_text = Graphics.StringFormat(Graphics.ALIGNMENT_LEFT, Graphics.ALIGNMENT_CENTER)
format_fps = Graphics.StringFormat(Graphics.ALIGNMENT_RIGHT, Graphics.ALIGNMENT_BOTTOM)

# area to draw text in
rect_fps = Game.Rect(0, 0, display_info.current_w - 4, display_info.current_h - 4)
rect_time = Game.Rect(0, 0, display_info.current_w, display_info.current_h)
rect_text = Game.Rect(0, 4, 1920, 200)

text_color = (241, 241, 241)

screen = Game.display.set_mode((display_info.current_w, display_info.current_h), Game.NOFRAME | Game.HWSURFACE)

default_font = Game.font.SysFont(None, 250)
fps_font = Game.font.SysFont('Consolas', 12)
username_font = Game.font.SysFont('Consolas', 14)
username_font.set_bold(True)

Game.mouse.set_visible(False)


def now_time(now, regex_format):
    return date_time.datetime.strftime(now, regex_format)

while True:
    current_time = now_time(date_time.datetime.now(), time_regex)

    for event in Game.event.get():
        if event.type == Game.QUIT:
            Game.quit()
            sys.exit()
        elif event.type in (Game.KEYUP, Game.KEYDOWN):
            key = Game.key.get_pressed()
            if event.key == Game.K_F4 and (key[Game.K_LALT] or key[Game.K_RALT]) or key[Game.K_ESCAPE]:
                Game.quit()
                sys.exit()

    screen.fill(0x1F1F1F)

    Graphics.draw_string(screen, 'FPS: ' + str(math.ceil(time_game.get_fps())),
                           rect_fps, fps_font, format_fps, text_color)
    Graphics.draw_string(screen, now_time(date_time.datetime.now(), time_regex),
                           rect_time, default_font, format_time, text_color)
    Game.draw.rect(screen, (255, 0, 0), (0, 0, 1920, 1080), 4)

    Game.draw.rect(screen, (0, 0, 0), (600, 150, 400, 200))
    Graphics.draw_string(screen, "Going to write out a very long string to try and fill up this text box.\n"
                                 "Let's see how long I can make this and still have it "
                                 " make sense!!!!!!!\n"
                                 "It's getting pretty long guys. I hope you're ready!\n\n\n\nHello world! :D\n\n~Signed\n    Author"
                                 "\nEnding line 1\nEnding line 2\nEnding line 3\nEnding line 4 - This line will not be shown",
                           Game.Rect(600 + 4, 150 + 4, 400 - 8, 200 - 4), fps_font, Graphics.StringFormat(Graphics.ALIGNMENT_RIGHT), (255, 0, 0))
    Game.draw.rect(screen, (128, 128, 128), (display_info.current_w - 104, 4, 100, 25))
    Graphics.draw_string(screen, username,
                           Game.Rect(display_info.current_w - 104, 4, 104, 25), username_font, Graphics.StringFormat(Graphics.ALIGNMENT_CENTER, Graphics.ALIGNMENT_CENTER), (255, 255, 255))


    Game.display.update()
    time_game.tick(60)

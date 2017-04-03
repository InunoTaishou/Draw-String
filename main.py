import pygame as Game
import datetime as date_time
import os
import math
import Graphics

# window will start at 0, 0
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
time_regex = '%I:%M %p\n%A, %h %d'

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

screen = Game.display.set_mode((display_info.current_w, display_info.current_h), Game.NOFRAME | Game.HWSURFACE)

default_font = Game.font.SysFont(None, 195)
fps_font = Game.font.SysFont('Consolas', 12)

Game.mouse.set_visible(False)


def now_time(now, regex_format):
    return date_time.datetime.strftime(now, regex_format)

while True:
    time_game.tick(30)

    current_time = now_time(date_time.datetime.now(), time_regex)

    event = Game.event.poll()
    key = Game.key.get_pressed()
    
    if event.type == Game.QUIT or (event.type == Game.KEYDOWN and ((event.key == Game.K_F4 and (key[Game.K_LALT] or key[Game.K_RALT])) or event.key == Game.K_ESCAPE)):
        Game.quit()
        exit(0)
    else:
        screen.fill(0x1F1F1F)
        Graphics.draw_string(screen, 'FPS: ' + str(math.ceil(time_game.get_fps())),
                           rect_fps, fps_font, format_fps, (255, 255, 255))
        Graphics.draw_string(screen, now_time(date_time.datetime.now(), time_regex),
                           rect_time, default_font, format_time, (241, 241, 241))
        Graphics.draw_string(screen, "Greetings!\n"
                                   "The secret to the universe is 42 but this line won't actually be shown!",
                           rect_text, default_font, format_text, (255, 0, 0))
        Game.draw.rect(screen, (255, 0, 0), (0, 0, display_info.current_w, display_info.current_h), 2)
        Game.display.update()
        prev_time = current_time
        # exit(0)

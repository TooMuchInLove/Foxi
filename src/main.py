# -*- coding: utf-8 -*-

from ui import Window
from services import Engine2D, Hero, Stationary, loading_sprites
from config import WIDTH, HEIGHT, TITLE, SPRITES


if __name__ == "__main__":
    window = Window(WIDTH, HEIGHT, "/fox.ico", "/background/bg2.png", TITLE)
    game = Engine2D(window)
    w, h = window.size
    game.loop(
        Hero(window.screen, w, h, loading_sprites(SPRITES["fox"])),
        Stationary(window.screen, w*0, h, loading_sprites(SPRITES["bush"]))
    )

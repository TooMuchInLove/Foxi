# -*- coding: utf-8 -*-

from config import WIDTH, HEIGHT, DIR_IMG, SPRITES, TITLE
from fox import HeroFox
from engine import Engine
from stationary import Stationary
from services import loading_sprites


if __name__ == "__main__":
    game = Engine()
    screen = game.window(WIDTH, HEIGHT, TITLE, DIR_IMG+"/fox.ico", DIR_IMG+"/background/bg2.png")
    w, h = game.get_size()
    fox = HeroFox(screen, w, h, loading_sprites(SPRITES["fox"]))
    bush0 = Stationary(screen, w*0, h, loading_sprites(SPRITES["bush"]))
    game.loop(fox=fox, bush=bush0)

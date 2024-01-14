# -*- coding: utf-8 -*-

from ui import Window
from services import Engine2D
from config import WIDTH, HEIGHT, TITLE


if __name__ == "__main__":
    window = Window(WIDTH, HEIGHT, "/fox.ico", "/background/bg2.png", TITLE)
    game = Engine2D(window)
    game.loop()

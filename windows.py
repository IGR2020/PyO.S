from loader import *
import pygame as pg


class Window(pg.Rect, pg.Surface):
    def __init__(self, x, y, width, height, flags=0, depth=0):
        pg.Rect.__init__(x, y, width, height)
        pg.Surface.__init__(size=(width, height), flags=flags, depth=depth)

    def display(): ...

    def close(): ...

    def resize(): ...


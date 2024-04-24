from loader import *
import pygame as pg
from store import load_data, save_data, getSize


class Window(pg.Rect):
    def __init__(self, x, y, width, height, surface: pg.Surface):
        pg.Rect.__init__(x, y, width, height)
        self.window = surface
    def display(): ...

    def close(): ...

    def resize(self, width, height): ...

    def install(): ...

class ThisPC(Window):
    def __init__(self, x, y, width, height, flags=0, depth=0):
        super().__init__(x, y, width, height, flags, depth)
        self.data = load_data("AppData\\This PC.pkl")

    def install():
        data = {"Available Storage": "~", "Used Storage": getSize("AppData")}
        save_data("AppData\\This PC.pkl", data)

    def display(self):
        self.window.blit((255, 255, 255))



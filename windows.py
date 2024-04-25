from loader import *
import pygame as pg
from store import load_data, save_data, getSize
from EPT import Button


class Window(pg.Rect):
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height)
        self.window = pg.Surface((width, height))
        self.decorator = WindowDecorator(x, y-DECORATOR_SIZE, width, DECORATOR_SIZE, name)

    def display(): ...

    def close(): ...

    def resize(self, width, height): ...

    def install(): ...

    def move(self, rel_x, rel_y): # call when grabed for movement
        self.x += rel_x
        self.y += rel_y
        self.decorator.move(rel_x, rel_y)


class ThisPC(Window):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "This P.C")
        self.data = load_data("AppData\\This PC.pkl")

    def install():
        data = {"Available Storage": "~", "Used Storage": getSize("AppData")}
        save_data("AppData\\This PC.pkl", data)

    def display(self, screen: pg.Surface):
        self.window.fill((255, 255, 255))
        self.decorator.display(screen)
        screen.blit(self.window, self)

    def close(self):
        pass


class WindowDecorator(pg.Rect):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height)
        self.name = name
        self.close_button = Button(
            (self.right - self.height, self.y),
            pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Close"], (self.height, self.height)
            ),
        )

    def display(self, screen: pg.Surface):
        pg.draw.rect(screen, (255, 255, 255), self)
        self.close_button.display(screen)

    def close(self): # call only if mouse is down
        return self.close_button.clicked() # returns T/F value
    
    def grab(self): # call only if button clicked checks have been completed and mouse down
        return self.collidepoint(pg.mouse.get_pos()) # returns T/F value
    
    def move(self, rel_x, rel_y): # call when grabed
        self.x += rel_x
        self.y += rel_y
        self.close_button.x += rel_x
        self.close_button.y += rel_y

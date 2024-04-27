from loader import *
import pygame as pg
from store import load_data, save_data, getSize
from EPT import Button, blit_text, load_assets


class Window(pg.Rect):
    def __init__(self, x, y, width, height, name=None, *args):
        super().__init__(x, y, width, height)
        self.window = pg.Surface((width, height))
        self.decorator = WindowDecorator(x, y-DECORATOR_SIZE, width, DECORATOR_SIZE, name)

    def display(): ...

    def close(self): ...

    def resize(self, width, height):
        self.width = width - DECORATOR_SIZE
        self.height = height
        self.window = pg.transform.scale(self.window, (self.width, self.height))

    def install(): ...

    def fullScreen(self, window_width, window_height):
        self.width = window_width - DECORATOR_SIZE
        self.height = window_height
        self.window = pg.transform.scale(self.window, (self.width, self.height))

    def resizeDecorator(self):
        self.decorator.width = self.width
        self.decorator.height = DECORATOR_SIZE
        self.decorator.updateButtons()

    def rePosition(self, x, y):
        self.x = x
        self.y = y
        self.decorator.x = x
        self.decorator.y = y-DECORATOR_SIZE
        self.decorator.updateButtons()

    def move(self, rel_x, rel_y): # call when grabed for movement
        self.x += rel_x
        self.y += rel_y
        self.decorator.move(rel_x, rel_y)

    def update(*args): ...


class ThisPC(Window):
    def __init__(self, x, y, width, height, *args):
        super().__init__(x, y, width, height, "This P.C")
        self.data = load_data("AppData\\This PC.pkl")
        self.assets = load_assets("assets\\This P.C")
        self.reSizedBackGround = pg.transform.scale(self.assets["BackGround1"], (self.width, self.height))

    def install(*args):
        total, break_down = getSize("AppData")
        data = {"Available Storage": "~", "Used Storage": total, "Break Down": break_down}
        save_data("AppData\\This PC.pkl", data)

    def display(self, screen: pg.Surface):
        self.window.fill((255, 255, 255))
        self.window.blit(self.reSizedBackGround, (0, 0))
        for y, file in enumerate(self.data["Break Down"]):
            blit_text(self.window, file, (30, y*30), size=20, colour=(255, 255, 255))
            blit_text(self.window, f"{self.data["Break Down"][file]} Bytes", (400, y*30), size=20, colour=(255, 255, 255))
        self.decorator.display(screen)
        screen.blit(self.window, self)

    def fullScreen(self, window_width, window_height):
        super().fullScreen(window_width, window_height)
        self.reSizedBackGround = pg.transform.scale(self.assets["BackGround1"], (self.width, self.height))
        self.resizeDecorator()
        self.rePosition(0, 0+DECORATOR_SIZE)

    def resize(self, width, height):
        super().resize(width, height)
        self.reSizedBackGround = pg.transform.scale(self.assets["BackGround1"], (width, height-DECORATOR_SIZE))
        self.resizeDecorator()
        self.rePosition(0, 0+DECORATOR_SIZE)

    def update(self):
        self.install()
        self.data = load_data("AppData\\This PC.pkl")


class WindowDecorator(pg.Rect):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height)
        self.name = name
        self.close_button = Button(
            (self.right - self.height, self.y),
            pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Close"], (self.height, self.height)
            ),
            1,
            "Close"
        )
        self.resize_button = Button(
            (self.right - self.height*2, self.y),
            pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Maximise"], (self.height, self.height)
            ),
            1,
            "Maximise"
        )

    def display(self, screen: pg.Surface):
        pg.draw.rect(screen, (255, 255, 255), self)
        self.close_button.display(screen)
        self.resize_button.display(screen)

    def close(self): # call only if mouse is down
        return self.close_button.clicked() # returns T/F value
    
    def resize(self): # call only if mouse is down
        if self.resize_button.clicked():
            if self.resize_button.info == "Maximise":
                self.resize_button.image = pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Fit"], (self.height, self.height)
            ) 
                self.resize_button.info= "Fit"
                return True, "Maximise"
            elif self.resize_button.info == "Fit":
                self.resize_button.image = pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Maximise"], (self.height, self.height)
            )
                self.resize_button.info = "Maximise"
                return True, "Fit"
        else:
            return False, None
        # returns T/F value
    
    def grab(self): # call only if button clicked checks have been completed and mouse down
        return self.collidepoint(pg.mouse.get_pos()) # returns T/F value
    
    def move(self, rel_x, rel_y): # call when grabed
        self.x += rel_x
        self.y += rel_y
        self.close_button.x += rel_x
        self.close_button.y += rel_y
        self.resize_button.x += rel_x
        self.resize_button.y += rel_y

    def updateButtons(self):
        self.close_button = Button(
            (self.right - self.height, self.y),
            pg.transform.scale(
                WINDOW_DECORATOR_ICONS["Close"], (self.height, self.height)
            ),
            1,
            "Close"
        )
        self.resize_button = Button(
            (self.right - self.height*2, self.y),
            pg.transform.scale(
                self.resize_button.image, (self.height, self.height)
            ),
            1,
            self.resize_button.info
        )

class BenchMarker(Window):
    def __init__(self, x, y, width, height, clock: pg.time.Clock, *args):
        super().__init__(x, y, width, height, "BenchMarker")
        self.clock = clock

    def display(self, screen):
        self.window.fill((0, 0, 0))
        blit_text(self.window, "FPS", (10, 10), (255, 255, 255), size=30)
        blit_text(self.window, round(self.clock.get_fps()), (10, 50), (255, 255, 255), size=30)
        self.decorator.display(screen)
        screen.blit(self.window, self)



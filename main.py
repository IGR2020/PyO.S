from loader import *
import pygame as pg
from icons import renderIcons

window = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.RESIZABLE)
pg.display.set_caption("Windows PyTop")

clock = pg.time.Clock()

run = True


# Display Function
def display():
    window.fill((255, 255, 255))
    window.blit(localWallPaper, (0, 0))
    renderIcons(window, WIDTH, HEIGHT, icon_size)
    pg.display.update()


# Main App Loop (M.A.P)
while run:

    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.VIDEORESIZE:
            WIDTH, HEIGHT = event.dict["size"]
            localWallPaper = pg.transform.scale(WALLPAPERS[selected_wallpaper], (WIDTH, HEIGHT))
            icon_size = ICON_WIDTH_RATIO*WIDTH
            for icon_name in ICON_NAMES:
                ReSizedIcons[icon_name] = pg.transform.scale(ICONS[icon_name], (icon_size, icon_size))
    display()
pg.quit()
quit()
    

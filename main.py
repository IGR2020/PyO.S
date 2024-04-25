from loader import *
import pygame as pg
from icons import generateIconButtons, getIconNameLink
from windows import ThisPC

window = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.RESIZABLE)
pg.display.set_caption("Windows PyTop")

clock = pg.time.Clock()

run = True

mouse_down = False

grabed_app = None

selected = False # bool for checking if a previous obj was selected when mouse down

icons = generateIconButtons(WIDTH, HEIGHT, icon_size)

running_apps = [ThisPC(100, 100, 800, 500)]


# Display Function
def display():
    window.fill((255, 255, 255))
    window.blit(localWallPaper, (0, 0))
    for icon in icons:
        icon.display(window)
    for app in running_apps:
        app.display(window)
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

            icons = generateIconButtons(WIDTH, HEIGHT, icon_size)

        if event.type == pg.MOUSEBUTTONDOWN:

            mouse_down = True
            selected = False

            if selected:
                continue

            for i, app in enumerate(running_apps):

                if app.decorator.close():
                    app.close()
                    running_apps.remove(app)
                    selected = True
                    break

                elif app.decorator.grab():
                    grabed_app = i
                    selected = True
                    break
            
            if selected:
                continue

            for icon in icons:
                if icon.clicked():
                    running_apps.append(getIconNameLink(icon.info)(icon.x, icon.y, 1000, 600))
                    selected = True

        if event.type == pg.MOUSEBUTTONUP:
            mouse_down = False
            grabed_app = None

    rel_x, rel_y = pg.mouse.get_rel()
    if mouse_down and grabed_app is not None:
        running_apps[i].move(rel_x, rel_y)
    display()

pg.quit()
quit()
    

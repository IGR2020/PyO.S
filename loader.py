# Loader loades assets and constants

import pygame as pg
from EPT import load_assets

WIDTH, HEIGHT = 1200, 650

FPS = 60

WALLPAPERS = load_assets("assets\\BackGrounds")
selected_wallpaper = "WallPaper1"
localWallPaper = pg.transform.scale(WALLPAPERS[selected_wallpaper], (WIDTH, HEIGHT))

icon_size = 64
ICON_WIDTH_RATIO = icon_size / WIDTH
ICONS = load_assets("assets\\Icons", (icon_size, icon_size))
ReSizedIcons = load_assets("assets\\Icons", (icon_size, icon_size))
ICON_NAMES = list(ICONS.keys())
iconDisplayMargins = 30
# Icon Related Content

from loader import *
import pygame as pg


def renderIcons(screen: pg.Surface, width, height, icon_size):
    icon_index = 0
    for y in range(round(height / icon_size)):
        for x in range(round(width / icon_size)):
            screen.blit(
                ReSizedIcons[ICON_NAMES[icon_index]],
                (
                    x * icon_size + x * (icon_size * 0.2) + iconDisplayMargins,
                    y * icon_size + y * (icon_size * 0.2) + iconDisplayMargins,
                ),
            )
            icon_index += 1
            if icon_index >= len(ICON_NAMES):
                return

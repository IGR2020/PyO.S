# Icon Related Content

from loader import *
import pygame as pg
from EPT import Button
from windows import ThisPC, Window, BenchMarker


def generateIconButtons(width, height, icon_size):
    icons = []
    icon_index = 0
    for y in range(round(height / icon_size)):
        for x in range(round(width / icon_size)):
            icons.append(
                Button(
                    (
                        x * icon_size + x * (icon_size * 0.2) + iconDisplayMargins,
                        y * icon_size + y * (icon_size * 0.2) + iconDisplayMargins,
                    ),
                    ReSizedIcons[ICON_NAMES[icon_index]],
                    1,
                    ICON_NAMES[icon_index],
                )
            )
            icon_index += 1
            if icon_index >= len(ICON_NAMES):
                return icons
    return icons


def getIconNameLink(name):
    if name == "This P.C": return ThisPC
    elif name == "BenchMarker": return BenchMarker
    else: return Window

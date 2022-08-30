import cv2
import numpy as np


def total_ui(mag, bg, x, y):

    if mag == 0:
        v = 0
        cv2.rectangle(bg, (x, y), (x+15, y+15), (v, v, v), -1)
    else:
        v = 255 * int(mag) / 100
        cv2.rectangle(bg, (x, y), (x+15, y+15), (v, v, v), -1)

    return bg

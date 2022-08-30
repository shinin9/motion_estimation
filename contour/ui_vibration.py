import cv2
import numpy as np


def ui_vib(vestIdx, w, h):
    background = np.full((h, w, 3), 0, np.uint8)
    #cv2.line(background, (1280//4, 0), (1280//4, 720), (255, 255, 255))
    #cv2.line(background, (1280//4*3, 0), (1280//4*3, 720), (255, 255, 255))

    x = w//8//2
    y = h//5//2
    for i in range(len(vestIdx)):
        if vestIdx[i] < 10:
            v = 255
            cv2.circle(background, (x, y), h//12, (v, v, v))
        else:
            v = 255*vestIdx[i]/100
            cv2.circle(background, (x, y), h//12, (v, v, v), -1)
        x += w // 8
        if (i+1) % 8 == 0:
            x = w//8//2
            y = y + h // 5

    return background
0
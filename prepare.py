import numpy as np
import cv2
from time import sleep
#idx = np.zeros([5, 8])
bg_h = 480
bg_w = 720
def idx_ui(idx, v):
    background = np.full((bg_h, bg_w, 3), 0, np.uint8)
    background[:] = (255, 255, 255)
    bg_vib = np.full((bg_h//2, bg_w, 3), 0, np.uint8)
    bg_vest = np.full((bg_h//2, bg_w, 3), 0, np.uint8)


    vest = cv2.imread(f'vest/{v}.png')
    vest = cv2.resize(vest, (bg_w // 2, bg_h // 2), interpolation=cv2.INTER_CUBIC)
    bg_vest[:, bg_w//2 - bg_w//4:bg_w//2 + bg_w//4] = vest


    x = 0
    y = 0
    z = bg_w // 8 // 2
    w = bg_h//2 // 5 // 2
    for i in range(5):
        for j in range(8):
            if idx[i][j] == 1:
                cv2.rectangle(background, (x, y), (x + bg_w // 8, y + bg_h // 5), (0, 127, 255), -1)
                cv2.circle(bg_vib, (z, w), bg_h//2 // 12, (255, 255, 255), -1)
            else:
                cv2.rectangle(background, (x, y), (x + bg_w // 8, y + bg_h // 5), (100, 100, 100))
                cv2.circle(bg_vib, (z, w), bg_h//2 // 12, (255, 255, 255))
            z += bg_w // 8
            x += bg_w // 8
            if (j+1) == 8:
                z = bg_w // 8 // 2
                w = w + bg_h//2 // 5
                x = 0
                y = y + bg_h // 5
        a = np.concatenate((bg_vib, bg_vest), axis=0)
        concat = np.concatenate((background, a), axis=1)

    return concat


#bg = idx_ui(idx)
#cv2.imshow('bg', bg)

#cv2.waitKey(0)

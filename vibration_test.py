from time import sleep
from bhaptics import better_haptic_player as player
import keyboard
import cv2
from prepare import idx_ui
import numpy as np

player.initialize()

interval = 0.5
durationMillis = 500
intensity = 100

A1 = [1, 5, 9, 13, 17]
A2 = [0, 4, 8, 12, 16]
A3 = [0, 4, 8, 12, 6]
A4 = [1, 5, 9, 13, 17]
B1 = [2, 6, 10, 14, 18]
B2 = [3, 7, 11, 15, 19]
B3 = [3, 7, 11, 15, 19]
B4 = [2, 6, 10, 14, 18]
H1 = [1, 0, 0, 1, 2, 3, 3, 2]
H2 = [5, 4, 4, 5, 6, 7, 7, 6]
H3 = [9, 8, 8, 9, 10, 11, 11, 10]
H4 = [13, 12, 12, 13, 14, 15, 15, 14]
H5 = [17, 16, 16, 17, 18, 19, 19, 18]

idx = np.zeros([5, 8])

def play(index):
    if index == 1:  # A1
        for n, i in enumerate(A1):
            idx_arr = idx.copy()
            idx_arr[n, 3] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A1')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 2:    # A2
        for n, i in enumerate(A2):
            idx_arr = idx.copy()
            idx_arr[n, 2] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A2')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 3:    # A3
        for n, i in enumerate(A3):
            idx_arr = idx.copy()
            idx_arr[n, 1] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A3')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 4:    # A4
        for n, i in enumerate(A4):
            idx_arr = idx.copy()
            idx_arr[n, 0] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A4')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 5:    # B1
        for n, i in enumerate(B1):
            idx_arr = idx.copy()
            idx_arr[n, 4] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B1')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 6:    # B2
        for n, i in enumerate(B2):
            idx_arr = idx.copy()
            idx_arr[n, 5] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B2')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 7:    # B3
        for n, i in enumerate(B3):
            idx_arr = idx.copy()
            idx_arr[n, 6] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B3')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 8:    # B4
        for n, i in enumerate(B4):
            idx_arr = idx.copy()
            idx_arr[n, 7] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B4')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 9:  # H1
        for n, i in enumerate(H1):
            idx_arr = idx.copy()
            idx_arr[0][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H1')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 10:  # H2
        for n, i in enumerate(H2):
            idx_arr = idx.copy()
            idx_arr[1][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H2')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 11:  # H3
        for n, i in enumerate(H3):
            idx_arr = idx.copy()
            idx_arr[2][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H3')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 12:  # H4
        for n, i in enumerate(H4):
            idx_arr = idx.copy()
            idx_arr[3][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H4')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 13:  # H5
        for n, i in enumerate(H1):
            idx_arr = idx.copy()
            idx_arr[4][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H5')
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)


def run():

    print("Press z to quit")
    while True:
        bg = idx_ui(idx, 0)
        cv2.imshow('bg', bg)
        cv2.waitKey(1)
        key = keyboard.read_key()
        if key == "z":
            break
        elif key == "1":
            play(1)
        elif key == "2":
            play(2)
        elif key == "3":
            play(3)
        elif key == "4":
            play(4)
        elif key == "5":
            play(5)
        elif key == "6":
            play(6)
        elif key == "7":
            play(7)
        elif key == "8":
            play(8)
        elif key == "q":
            play(9)
        elif key == "w":
            play(10)
        elif key == "e":
            play(11)
        elif key == "r":
            play(12)
        elif key == "t":
            play(13)

#        if cv2.waitKey(1) == ord('q'):
#            break



if __name__ == "__main__":

    run()

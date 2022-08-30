import cv2
import pickle
import torch
import time
import math
from PIL import Image
import pafy


videoUrl_1 = 'https://www.youtube.com/watch?v=AH9KheHIj2g' #love dive
videoUrl_2 = 'https://www.youtube.com/watch?v=zW28Mb1YvwY' #비행기
videoUrl_3 = 'https://www.youtube.com/watch?v=nMw-PspfdkQ' #비행기2

videoPafy = pafy.new(videoUrl_3)
cap = cv2.VideoCapture(videoPafy.streams[-1].url)


w = cap.get(3)
h = cap.get(4)
fps = cap.get(5)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(f'/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/new_video/fishingbird.avi', fourcc, fps, (int(w), int(h)))



while cap.isOpened():


    # Read frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    # frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Estimated flow", frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break
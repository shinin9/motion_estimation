from bhaptics import better_haptic_player as player
import pickle
import cv2
import os

path = 'C:/Users/heat/Desktop/bhaptics_project_yj/bhaptics_project_yj/video_data/'
video_list = os.listdir(path)
# video_list = ['ball2.mp4']

#video_path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/doc/data/traffic.mp4'
for video in video_list:
    video_path = path + video
    video_name = video_path.split('/')[-1][:-4]

    w = 1280
    h = 720
    a = 0
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_CUBIC)
        if a == 0:
            cv2.imwrite(f'ff/{video_name}_first.jpg', frame)
            break

        cv2.imshow("test", frame)



        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()



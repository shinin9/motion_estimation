import cv2
import numpy as np
from mapping import mapping_function, make_dict
from ui_vibration import ui_vib
import pickle


path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/video_last/'
video_path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/video_last/plane_Trim_Trim_Trim.mp4'
mag_arr_list = []
video_name = video_path.split('/')[-1][:-4]
cap = cv2.VideoCapture(video_path)

w = 640
h = 480
fps = cap.get(5)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(f'/Users/heat/PycharmProjects/contour/contour_data_output/edge_{video_name}.avi', fourcc, fps, (int(w)*2 , int(h)))

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
bg_h = 40 * 15
bg_w = length * 15

bg = np.full((bg_h, bg_w, 3), 0, np.uint8)
bg_x = bg_w // length
yy = bg_h // 40
bg_y = yy
frame_list = []
frame_num = 0


while cap.isOpened():
    try:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (w,h), interpolation=cv2.INTER_CUBIC)

    except:
        continue


    vestIdx = make_dict()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

    vestIdx = mapping_function(contours, w, h, vestIdx)

    ui = ui_vib(vestIdx, w, h)
    image_copy = frame.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    concat = np.concatenate((image_copy, ui), axis=1)

    out.write(concat)
    vestIdx = np.array(vestIdx)
    vestIdx = vestIdx.reshape(5, 8)
    mag_arr_list.append(vestIdx)
    cv2.imshow('output', concat)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# with open(f'/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/mag_edge/ppt_edge_{video_name}', 'wb') as fw:
#     pickle.dump(mag_arr_list, fw)

import os
import numpy as np
import argparse
import cv2
import pickle
import torch
import time
import math
from PIL import Image
import pafy
from raft import Raft
from ui2 import total_ui

import gc

gc.collect()
torch.cuda.empty_cache()

FLOW_FRAME_OFFSET = 10 # Number of frame difference to estimate the optical flow

# Initialize model
model_path='models/raft_sintel_iter20_360x480.onnx'
flow_estimator = Raft(model_path)

# videoUrl = 'https://www.youtube.com/watch?v=YcskSSCBslg' #농구공
# videoUrl = 'https://www.youtube.com/watch?v=PKt9-zN-31I' #농구공2
# videoPafy = pafy.new(videoUrl)
# cap = cv2.VideoCapture(videoPafy.streams[-1].url)

mag_arr_list = []

io_time = []
pad_time = []
infer_time = []
conv_time = []

path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/video_last/'
# video_path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/doc/data/Eagle.mp4'
video_list = os.listdir(path)
# video_list = ['Fall.mp4', 'WaterDrop.mp4', 'traffic.mp4', 'Baseball_slow.avi']
#
video_path = path + 'plane_Trim_Trim_Trim.mp4'
video_name = video_path.split('/')[-1][:-4]
video_name = 'plane'
model_name = 'sintel_2'

start_time = 1
# cap.set(cv2.CAP_PROP_POS_FRAMES, start_time*30)

# cv2.namedWindow("Estimated flow", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(video_path)

# w = int(cap.get(3))
# h = int(cap.get(4))
w = 640
h = 480
fps = cap.get(5)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(f'/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/data_output/{video_name}.avi', fourcc, fps, (int(w) * 2, int(h)))
out2 = cv2.VideoWriter(f'{video_name}.mp4', fourcc, fps, (int(w), int(h)))

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
bg_h = 40 * 15
bg_w = length * 15

bg = np.full((bg_h, bg_w, 3), 0, np.uint8)
bg_x = bg_w // length
yy = bg_h // 40
bg_y = yy
frame_list = []
frame_num = 0
# ret, prev_frame = cap.read()
while cap.isOpened():

	try:
		# Read frame from the video
		ret, prev_frame = cap.read()
		if not ret:
			break
		prev_frame = cv2.resize(prev_frame, (w, h), interpolation=cv2.INTER_CUBIC)
		frame_list.append(prev_frame)

	except:
		continue

	# Skip the first frames to be able to
	frame_num += 1
	if frame_num <= FLOW_FRAME_OFFSET:
		continue


	flow_map = flow_estimator(frame_list[0], frame_list[-1])
	print(flow_map)
	flow_img = flow_estimator.draw_flow()

	flow_mag = np.sqrt(np.square(flow_map[:,:,0]) + np.square(flow_map[:,:,1]))
	flow_mag = np.where(flow_mag < 1, 0, flow_mag)
	flow_mag = cv2.resize(flow_mag, (w,h))

	# flow_mag = flow_mag / 40
	# flow_mag = flow_mag / 186
	# flow_mag = np.where(flow_mag < 1, 0, flow_mag)
	# max_mag.append(torch.max(flow_mag))
	vest_w = 8
	vest_h = 5

	img_w = flow_mag.shape[1]
	img_h = flow_mag.shape[0]

	step_w = math.floor(img_w / vest_w)
	step_h = math.floor(img_h / vest_h)

	mag_arr = np.zeros([vest_h, vest_w])
	background = np.full((img_h, img_w, 3), 0, np.uint8)
	x = img_w // 8 // 2
	y = img_h // 5 // 2

	dotFrame_F = {
		"Position": "VestFront",
		"DotPoints": [],
		"DurationMillis": 1000
	}
	dotFrame_B = {
		"Position": "VestBack",
		"DotPoints": [],
		"DurationMillis": 1000
	}
	v = 0
	for i in range(vest_h):
		for j in range(vest_w):
			mag_arr[i][j] = int(np.sum(flow_mag[i * step_h:(i + 1) * step_h, j * step_w:(j + 1) * step_w]))
			if mag_arr[i][j] > 100:
				mag_arr[i][j] = 100
			elif mag_arr[i][j] < 10:
				mag_arr[i][j] = 0

			if 2 <= j <= 5:
				dotPint = {
					"Index": int(v),
					"Intensity": int(mag_arr[i][j])
				}
				dotFrame_F["DotPoints"].append(dotPint)
			else:
				dotPint = {
					"Index": int(v),
					"Intensity": int(mag_arr[i][j])
				}
				dotFrame_B["DotPoints"].append(dotPint)

			bg = total_ui(mag_arr[i][j], bg, bg_x, bg_y)

			if mag_arr[i][j] == 0:
				c = 255
				cv2.circle(background, (x, y), img_h//12, (c, c, c))
			else:
				c = 255 * int(mag_arr[i][j]) / 100
				cv2.circle(background, (x, y), img_h//12, (c, c, c), -1)
			x += img_w // 8
			if (v + 1) % 8 == 0:
				x = img_w // 8 // 2
				y = y + img_h // 5
			v += 1
			if v % 5 == 0:
				bg_y = yy + bg_h // 40
				yy = bg_y
			else:
				bg_y += bg_h // 40 * 8
	yy = bg_h // 40
	bg_y = yy
	bg_x += bg_w // length
	# player.submit("dotPoint_F", dotFrame_F)
	# player.submit("dotPoint_B", dotFrame_B)

	# mag_arr = mag_arr.numpy()
	print(mag_arr)
	mag_arr_list.append(mag_arr)
	alpha = 0.5
	combined_img = cv2.addWeighted(frame_list[0], alpha, flow_img, (1-alpha),0)
	concat = np.concatenate((combined_img, background), axis=1)
	out.write(concat)
	out2.write(prev_frame)
	cv2.imshow("Estimated flow", concat)

	# Remove the oldest frame
	frame_list.pop(0)

	cv2.imwrite(f'/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/total_ui_img/{video_name}_{model_name}.jpg', bg)

	# Press key q to stop
	if cv2.waitKey(1) == ord('q'):
		break

with open(f'mag_flow/{video_name}', 'wb') as fw:
	pickle.dump(mag_arr_list, fw)

cap.release()
cv2.destroyAllWindows()


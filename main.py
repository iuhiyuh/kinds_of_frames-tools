# -*- coding: utf-8 -*-
import cv2
import os

from opts import parse_opts

opt = parse_opts()
opt.videos_path = opt.videos_path[0]
opt.target_path = opt.target_path[0]
opt.cut_start = opt.cut_start[0]
opt.cut_end = opt.cut_end[0]

i = 0
cut_start = opt.cut_start
cut_end = opt.cut_end

if not os.path.exists(opt.target_path):
    os.mkdir(opt.target_path)

for video in os.listdir(opt.videos_path):
    if ('.avi' or '.mp4') not in video:
      continue
    name, ext = os.path.splitext(video)
    opt.target_path = os.path.join(opt.target_path, name)
    if not os.path.exists(opt.target_path):
        os.mkdir(opt.target_path)
    cap = cv2.VideoCapture(os.path.join(opt.videos_path,video))
    success_get, frame = cap.read()
    while success_get:
        if cut_start - 1 <= i & i <= cut_end - 1:
            print("load: 第 %d 帧 / 从 %d 帧，到 %d 帧" % (i + 1, cut_start, cut_end))
            success_get, frame = cap.read()
            cv2.imencode(os.path.join(opt.target_path, str(i) + '.png'), frame)[1]\
                .tofile(os.path.join(opt.target_path, str(i) + '.png'))
        elif i > cut_end:
            break
        i += 1
        cv2.waitKey(1)
    cap.release()


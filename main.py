# -*- coding: utf-8 -*-
import cv2
import os

from opts import parse_opts

opt = parse_opts()
opt.videos_path = opt.videos_path[0]
opt.target_path = opt.target_path[0]
opt.cut_start = opt.cut_start[0]
opt.cut_end = opt.cut_end[0]

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
    cap.set(cv2.CAP_PROP_POS_FRAMES, cut_start)

    i = cut_start
    while True:
        success_get, frame = cap.read()
        if success_get:
            i += 1
            if cut_start < i & i < cut_end + 2:
                print("load: 第 %d 帧 / 从 %d 帧，到 %d 帧" % (i - 1, cut_start, cut_end))
                cv2.imencode(os.path.join(opt.target_path, str(i-1) + '.png'), frame)[1]\
                .tofile(os.path.join(opt.target_path, str(i-1) + '.png'))
            if i >= cut_end + 2:
                break
        else:
            break
        cv2.waitKey(1)
    cap.release()


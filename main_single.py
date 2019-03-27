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

if not os.path.exists("".join(opt.target_path)):
    os.mkdir("".join(opt.target_path))
cap = cv2.VideoCapture(opt.videos_path)
success_get, frame = cap.read()
while True:
    success_get, frame = cap.read()
    if success_get:
        i += 1
        if cut_start - 1 <= i & i <= cut_end - 1:
            print("load: 第 %d 帧 / 从 %d 帧，到 %d 帧" % (i + 1, cut_start, cut_end))
            cv2.imencode(os.path.join(opt.target_path, str(i) + '.png'), frame)[1] \
                .tofile(os.path.join(opt.target_path, str(i) + '.png'))
    else:
        break

    cv2.waitKey(1)
cap.release()

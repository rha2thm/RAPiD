#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from pathlib import Path

from api import Detector
from sort import Sort

if __name__=='__main__':
    # load model
    detector = Detector(model_name='rapid',
                        backbone='yolov5n',
                        weights_path='./weights/rapid_pL1_yolov5n_COCO608_Dec23_100000.ckpt',
                        use_cuda=False)
    #
    #  # detect from video
    vid_dts = detector.detect_video(video_dir='./images/illusion.mp4', input_size=608, conf_thres=0.3, sort=True, save_video=True)


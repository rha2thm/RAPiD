#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api import Detector

if __name__=='__main__':
    # load model
    detector = Detector(model_name='rapid',
                        backbone='yolov5n',
                        weights_path='./weights/rapid_pL1_yolov5n_CPHBMW608_Dec28_6000.ckpt',
                        use_cuda=False)

    #  # detect from video
    vid_dts = detector.detect_video(video_dir='./images/omni1A_test6.mp4',
                                    input_size=608,
                                    conf_thres=0.3,
                                    sort=True,
                                    save_video=True,
                                    show_angle=False)


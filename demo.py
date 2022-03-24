#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api import Detector

if __name__=='__main__':
    # load model
    detector = Detector(model_name='rapid',
                        backbone='yolov5m',
                        weights_path='./weights/rapid_pL1_yolov5m_CPHBMW608_Feb20_6000.ckpt',
                        use_cuda=True)

    #  # detect from video
    vid_dts = detector.detect_video(video_dir='./images/omni1B_test6.mp4',
                                    input_size=608,
                                    conf_thres=0.3,
                                    sort=True,
                                    save_video=True,
                                    show_angle=False)


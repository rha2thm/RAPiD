#!/bin/bash

python train.py --model rapid_pL1 \
                --backbone yolov5m \
                --dataset COCO \
                --batch_size 8 \
                --eval_interval 1000 \
                --img_interval 1000 \
                --checkpoint_interval 5000
                


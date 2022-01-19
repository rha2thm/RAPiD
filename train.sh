#!/bin/bash

python train.py --model rapid_pL1 \
                --backbone yolov5x \
                --dataset COCO \
                --batch_size 8 \
                --eval_interval 20 \
                --img_interval 100 \
                --checkpoint_interval 100
                


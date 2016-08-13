#!/usr/bin/env python3

import cv2
import numpy as np
import logging
import argparse
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("capture")

parser = argparse.ArgumentParser(description='Video Extracter')
parser.add_argument('--name', help='File name')
args = parser.parse_args()

# Run the following commands:
# v4l2-ctl -c exposure_auto=1 && v4l2-ctl -c exposure_absolute=5

def main():
    args = parser.parse_args()
    filename = args.name
    try:
        frame_cnt = 0
        logger.debug("reading from file %s" % filename)
        capture = cv2.VideoCapture(filename)
        logger.debug("capturing...")
        while capture.isOpened():
            ret, frame = capture.read()
            if ret:
                cv2.imwrite("result/field.%s.%d.jpg" % (filename, frame_cnt), frame)
                logger.debug("%d written" % frame_cnt)
                frame_cnt = frame_cnt + 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
    except KeyboardInterrupt:
        capture.release()

if __name__ == '__main__':
    main()

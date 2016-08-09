#!/usr/bin/env python3

import cv2
import numpy as np
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("capture")

parser = argparse.ArgumentParser(description='Video Capture')
parser.add_argument('--name', help='File name')
args = parser.parse_args()

# Run the following commands:
# v4l2-ctl -c exposure_auto=1 && v4l2-ctl -c exposure_absolute=5

def main():
    args = parser.parse_args()
    filename = args.name
    logger.debug("writing to %s" % filename)
    try:
        frame_cnt = 0
        logger.debug("connecting to mjpeg stream...")
        capture = cv2.VideoCapture("http://pi-frc-9036.local:5806/?action=stream")
        logger.debug("capturing...")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))
        while capture.isOpened():
            ret, frame = capture.read()
            out.write(frame)
            logger.debug("%d written" & frame_cnt)
            frame_cnt = frame_cnt + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        capture.release()
        out.release

if __name__ == '__main__':
    main()

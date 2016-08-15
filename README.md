# stronghold-video-capture

Video Capture script. Capture video from an mjpg stream and extract them into
image sequence.

## License

MIT

声明：我们允许组织以及个人将此项目用于商业行为，没有任何限制。
但**请带上本项目的许可证 `MIT`**，并**附上原作者以及项目的地址**。我们保留对该项目的最终解释权。

## Requirements

Python3, numpy and cv2 are required to run this script.

Install OpenCV 3.1 for Python3, and then install other requirements:

```
pip install -r requirements.txt
```

## Configure

Edit mjpg stream source url here:

```
capture = cv2.VideoCapture("http://pi-frc-9036.local:5801/stream.mjpg")  # Maybe http://localhost:8080/?action=stream
```

Edit output video parameters here:

```
out = cv2.VideoWriter(filename, fourcc, 24.0, (640, 480)) # filename, output type, fps, frame size
```

If you want to capture camera image at low exposure, install `v4l2`
and run these commands in bash (this can only apply to Microsoft LifeCam 3000):

```
v4l2-ctl -c exposure_auto=1 && v4l2-ctl -c exposure_absolute=5
```

## Run

To capture a video:

```
./capture.py --name test.mp4        (Linux)
python capture.py --name test.mp4   (Windows)
```

It may take about 20 seconds to connect to your video stream.

To extract a video:

```
mkdir result

./extract.py --name test.mp4        (Linux)
python extract.py --name test.mp4   (Windows)
```

Then each frame will be extracted to `result/field.test.mp4.xxx.jpg`.

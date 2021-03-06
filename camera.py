from datetime import datetime
from gpiozero import Button
import picamera
import time


def camera_module():
    return


def main():
    camera_module()


if __name__ == 'main':
    main()


button = Button(14)
pi_camera = picamera.PiCamera()
#pi_camera.resolution = (x, y)
running = True

timestamp = datetime.now()


def picture():
    # Take image and export it
    pi_camera.capture('picture{}.jpg').format(timestamp)


pi_camera.start_preview()
button.when_pressed = picture

try:
    while running:
        print('Camera is active.')
        time.sleep(1)
except KeyboardInterrupt:  # Ctrl + C
    pi_camera.stop_preview()
    running = False

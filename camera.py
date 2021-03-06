from datetime import datetime
from gpiozero import Button
from time import sleep
import picamera


def camera_module():
    return


def main():
    camera_module()


if __name__ == 'main':
    main()


# Main code
button = Button(14)
running = True


def timestamp():
    # Take image and export it
    timestamp = datetime.now()
    pi_camera.capture('picture{}.jpg').format(timestamp)


try:
    while running:
        pi_camera = camera.PiCamera()
        #pi_camera.resolution = (x, y)
        pi_camera.start_preview()
        button.when_pressed = picture(pi_camera)
        pi_camera.stop_preview()
        sleep(1)
except KeyboardInterrupt:  # Ctrl + C
    pi_camera.stop_preview()
    running = False

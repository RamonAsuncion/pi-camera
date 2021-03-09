from datetime import datetime
from gpiozero import Button
from time import sleep
import picamera

# Connected to GPIO14 pin on the rasberry pi
button = Button(14)
running = True


def timestamp():
    # Gets the date and time.
    timestamp = datetime.now()
    # Saves the file name as "picture + (date and time) + png"
    pi_camera.capture('picture{}.png').format(timestamp)


try:
    while running:
        pi_camera = camera.PiCamera()
        # pi_camera.resolution = (x, y) Resolution to be a specific width and height.
        pi_camera.start_preview()
        button.when_pressed = timestamp(pi_camera)
        pi_camera.stop_preview()
        sleep(1)
except KeyboardInterrupt:  # Ctrl + C to stop the code from running.
    pi_camera.stop_preview()
    running = False

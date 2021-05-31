from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(2)
camera.start_recording('/home/pi/vid.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
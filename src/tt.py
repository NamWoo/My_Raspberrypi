from picamera import PiCamera
from time import sleep


camera = PiCamera()
camera.start_preview()

sleep(90)

#camera.capture('/home/pi/capture.jpg')

camera.stop_preview()

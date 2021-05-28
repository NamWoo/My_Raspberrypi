import picamera
import time
import datetime

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    now = datetime.datetime.now()
    filename = now.strftime('%Y-%m-%d_%H:%M:%S.jpg')
    #camera.start_preview()
    time.sleep(1)

    camera.capture('/home/pi/Desktop/img/'+ filename)
    #camera.stop_preview()

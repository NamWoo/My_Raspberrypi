# -*- coding: utf-8 -*-
import picamera            #picamera를 불러온다.
import RPi.GPIO as GPIO    #GPIO 라이브러리
from time import sleep     #sleep 라이브러리
import datetime

#보기 편하도록 미리 상수처럼 선언함
HIGH = True                
LOW = False
ON  = True
OFF = False

#핀 
LED = 23
Button = 18

#GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Button, GPIO.IN)

#상태 변수들
recStat = False  #레코딩 상태
btnStat = HIGH   #버튼 상태
ledStat = OFF    #LED 상태
ledTimeCnt = 0   #LED 깜박임 시간 카운트

keyCheckTime = 0.1 # 버튼 입력 시간 

#LED 깜박이는 간격 1초로 설정
LEDBlankTime = 10


#LED 상태 초기화
def initLedStatus():
    ledTimeCnt  = 0
    ledStat = False
    GPIO.output(LED, OFF)

initLedStatus()
camera = picamera.PiCamera() # 카메라 ON
camera.resolution = (1024, 768)

print('Waiting for Button to Press')
try:
    while True:
        if GPIO.input(Button) == LOW:
            initLedStatus()
            if btnStat == HIGH:
                # print('push')
                
                if recStat == False:
                    GPIO.output(LED, ON)
                    # initLedStatus()
                    # print('pic')
                    now = datetime.datetime.now()
                    filename = now.strftime('%Y-%m-%d_%H:%M:%S.jpg')
                    filepath = '/home/pi/Desktop/img/'+ filename
                    camera.capture(filepath)
                    # print(filepath)
                    # print('Start Recording')
                    # recStat = True
                    
                        # ledStat = False
                    sleep(1)
                    initLedStatus()
                
                else:
                    initLedStatus()
                    # camera.stop_recording()
                    print('Stop Recording')
                    recStat = False
                
                # btnStat = LOW

            else:
                if btnStat == LOW:
                    print('pull')
                    btnStat = HIGH
				
         
            # if recStat == True:
            #     ledTimeCnt += 1
     
            #     if ledTimeCnt >= LEDBlankTime:
            #         ledTimeCnt = 0
            #         if ledStat == True:
            #             GPIO.output(LED, ON)
            #             ledStat = False
            #         else:
            #             GPIO.output(LED, OFF)
            #             ledStat = True
					
            sleep(keyCheckTime)
			
except KeyboardInterrupt:
    camera.close()
    GPIO.cleanup()

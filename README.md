# My_Raspberrypi
raspberry pi test


# raspi

```
# pic
raspistill -o test.jpg
raspistill -o test.jpg -t 10000 #10s, t는 밀리미터
raspistill -vf -o test2.jpg #-vf는 상하반전, -hf는 좌우반전

# video
raspivid -o vid.h264 # 5s
```

## 포맷변경

```
# 설치
sudo apt-get install -y gpac
# 변환
MP4Box -add vid3.h264 vid3.mp4
# 재생
omxplayer vid.h264
```





## installation

[opencv build shell script](./install/pi_opencv_build_1.sh)

* 참고
* [Raspberry Pi 4에 Extra Module(contrib) 포함하여 OpenCV 4.5.1 설치하는 방법](https://webnautes.tistory.com/916)
 

## GPIO

[source code](./src/with_btn)


* 참고
* [라즈베리 파이(Raspberry Pi) GPIO를 다뤄보기 - 파이썬](https://m.blog.naver.com/chandong83/220905339312)


![GPIO 설정](https://mblogthumb-phinf.pstatic.net/MjAxNzAxMDdfODkg/MDAxNDgzNzkyNTc1ODQx.Zdw5-gDt1C-gGmxLmFtIinNLpu3wi3URCGYTdVPmaakg.AfUxK97CsXchp0AEk5lJydHVXTVEkrhsgrxdft3V810g.JPEG.chandong83/image_5940415111483792559665.jpg?type=w800)


## chk

```python
python3 /usr/local/share/opencv4/samples/python/video.py
```



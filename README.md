# Camera Streaming and servomotor (in Orange Pi Zero)

* Enable pwm adding to overlays at */boot/armbianEnv.txt* file: `overlays=pwm`
* Reboot and run *scripts/init-pwm.sh* as superuser (required on every system restart).
* (Optional) run *scripts/test-pwm.sh* as normal user (should work) for testing.
* Install dependencies: `pip install -r requirements.txt`
* Run Server: `python app.py`

## Live Streaming with Flask and Open-CV

#### Use Built-in Webcam of Laptop
##### Put Zero (O) in cv2.VideoCapture(0) (if webcam is /dev/video0)
```python
cv2.VideoCapture(0)
```
#### Use Ip Camera/CCTV/RTSP Link
```python
cv2.VideoCapture('rtsp://username:password@camera_ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp')  
 ```
####  Example RTSP Link
```python
cv2.VideoCapture('rtsp://mamun:123456@101.134.16.117:554/user=mamun_password=123456_channel=0_stream=0.sdp')
```
#### Change Channel Number to Change the Camera
```python
cv2.VideoCapture('rtsp://mamun:123456@101.134.16.117:554/user=mamun_password=123456_channel=1_stream=0.sdp')
```
#### Display the resulting frame in browser
```python
cv2.imencode('.jpg', frame)[1].tobytes()                 
``` 
### Or this one

 ```python
net , buffer = cv2.imencode('.jpg', frame)
buffer.tobytes()              
```   

 ### Credit
 Learn More about Streaming with flask
 - https://blog.miguelgrinberg.com/post/video-streaming-with-flask

## Servomotor with PWM
### Wiring diagram
![Wiring diagram](/img/wiring.jpg)
#### Links
- SG90 servo: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf

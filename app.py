from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

# PWM stuff:
INCREMENT = 20000
MIN = 500000
MAX = 2000000

PWM_PATH = "/sys/class/pwm/pwmchip0/pwm0/duty_cycle"

camera = cv2.VideoCapture(1)  # In my case 1 from: "/dev/video1"

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/turn', methods=['POST'])
def turn_camera():
    direction = request.form.get('direction')
    print("Direction: " + direction)
    f = open(PWM_PATH, 'r+')
    actual_position = int(f.read())
    if direction == 'left' and actual_position < MAX:
        actual_position += INCREMENT
    elif direction == 'right' and actual_position > MIN:
        actual_position -= INCREMENT
    else:
        f.close()
        return "error: invalid argument"
    f.write("{}".format(actual_position))
    f.close()
    return "{}".format(actual_position)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

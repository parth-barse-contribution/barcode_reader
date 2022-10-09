# Import necessary libraries
from flask import Flask, render_template, Response
from pyzbar.pyzbar import decode
import cv2
# Initialize the Flask app
app = Flask(__name__)

camera = cv2.VideoCapture(1)

cam = True
r = ""
def gen_frames():
    global cam
    while cam == True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            decoding_info = decode(frame)
            if decoding_info:
                r=decoding_info[0].data.decode()
                print(decoding_info[0].data.decode())
                cam = False
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    global cam
    if cam == True:
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

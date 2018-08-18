from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import numbers


app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/controller')
def showController():
    return render_template('controller.html')

@app.route('/sensor')
def showSensor():
    return "this is the sensor view"



def ack():
    print "JS recieved the reply!"

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print("client has connected")

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send("we receieved your message: '" + message + "'")

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    emit()

@socketio.on('my event')
def handle_my_custom_event(json):
    print "PY: message recieved: " + json
    emit('hello from py, we saw your message: ' + json)

@socketio.on('plzSqr')
def squareNumber(num):
    if isinstance(num, numbers.Number):
        emit(num*num)
    else:
        print("request to square number :" + num)
        num = float(num)
        emit('plzSqr-res',num*num)
    #emit(num*num)

# run the application
if __name__ == "__main__":
    socketio.run(app)

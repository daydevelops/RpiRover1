from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import numbers
import sys

sys.path.append('robot-control')
import robotController
#import testdrive

#testdrive.initRobot()

#initializeRobot.sayHi()

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



@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print("client has connected")
    global robot 
    robot = RobotController.initRobot()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    #send("we receieved your message: '" + message + "'")

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    emit()

@socketio.on('accelData')
def addData(msg):
	robotController.driveRobot(robot,msg)

# run the application
if __name__ == "__main__":
    socketio.run(app,"192.168.2.19")

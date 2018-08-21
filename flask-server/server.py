from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import numbers
import sys

sys.path.append('robot-control')
import robotController

app = Flask(__name__)
socketio = SocketIO(app)


### FLASK PAGES ###
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/controller')
def showController():
    return render_template('controller.html')

@app.route('/sensor')
def showSensor():
    return "this is the sensor view"




### SOCKET IO EVENTS ###

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print("client has connected")

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    robot.stop()

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('initRobot')
def initRobot():
    global robot 
    robot = RobotController.initRobot()
	
@socketio.on('shutDownRobot')
def shutDownRobot():
	robot.stop()
	

@socketio.on('leftTrim')
def updateLeftTrim(trim):
	robot.setLeftTrim(trim)
	
@socketio.on('rightTrim') 
def updateRightTrim(trim):
	robot.setRightTrim(trim)

@socketio.on('accelData')
def addData(msg):
	print msg
	#robotController.driveRobot(robot,msg)




### run the application
if __name__ == "__main__":
    socketio.run(app,"192.168.2.19")

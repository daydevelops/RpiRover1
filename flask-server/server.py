from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
import numbers
import sys, json
import pprint

sys.path.append('robot-control')
import robotController # commented out while working on remote
sys.path.append('db')
import mongo
mdb = mongo.MDB()

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
def connect():
    print("client has connected")

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    # robot.stop() # commented out while working on remote

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('initRobot')
def initRobot():
    print('Initializing Robot')
    trims = mdb.getTrimValues()
    emit('initTrim',json.dumps(trims))
    global robot  # commented out while working on remote
    robot = robotController.initRobot(LEFT_TRIM=trims['L'],RIGHT_TRIM=trims['R'])

@socketio.on('shutDownRobot')
def shutDownRobot():
    print('Shutting Down Robot')
	# robot.stop() # commented out while working on remote


@socketio.on('leftTrim')
def updateLeftTrim(trim):
    print('Updating Left Motor Trim: ' + str(trim))
	# robot.setLeftTrim(trim) # commented out while working on remote

@socketio.on('rightTrim')
def updateRightTrim(trim):
    print('Updating right Motor Trim: ' + str(trim))
	# robot.setRightTrim(trim) # commented out while working on remote

@socketio.on('accelData')
def addData(msg):
	print msg
	#robotController.driveRobot(robot,msg)




### run the application
if __name__ == "__main__":
    socketio.run(app,"192.168.2.30")

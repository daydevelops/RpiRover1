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
import Logs

app = Flask(__name__)
# ping client every second
## if no response after 3, disconnect
socketio = SocketIO(app,ping_timeout=3,ping_interval=1)


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
    print "client has connected"
    print 'Initializing database'
    DB = Logs.Logs()
    trims = DB.getTrimValues()
    emit('initTrim',json.dumps(trims))
    global robot
    print('Initializing Robot')
    robot = robotController.initRobot(LEFT_TRIM=trims['L'],RIGHT_TRIM=trims['R'])


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    robotController.driveRobot(robot,{
        'speed':0,
        'heading':0
    })

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('shutDownRobot')
def shutDownRobot():
    print('Shutting Down Robot')
	# robot.stop() # commented out while working on remote


@socketio.on('updateTrim')
def updateTrim(change):
    global robot
    trim = robotController.updateTrim(robot,change['L'],change['R'])
    print('Updated Motor Trim' + json.dumps(trim))
    emit('initTrim',json.dumps(trim))

@socketio.on('speedInput')
def speedInput(data):
    robotController.driveRobot(robot,data)



### run the application
if __name__ == "__main__":
    socketio.run(app,"192.168.2.19")

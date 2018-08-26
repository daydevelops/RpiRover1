import json
import time
# import Robot
import sys
sys.path.append('db')
import Logs
DB = Logs.Logs()

def getTrimValues():
    return DB.getTrimValues()

def initRobot(LEFT_TRIM, RIGHT_TRIM):
    print "initializing robot with l_trim = "+str(LEFT_TRIM)+" and r_trim = "+str(RIGHT_TRIM)
    # robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
    # return robot

def driveRobot(robot,data):
	motorSpeeds = processAccData(data)
	robot.leftM(int(motorSpeeds['LM']))
	robot.rightM(int(motorSpeeds['RM']))

def updateTrim(robot,changeL,changeR):
    # get trim from db
    trims = getTrimValues()
    ltrim = trims['L']
    rtrim = trims['R']
    # add chagne value
    ltrim = ltrim + changeL
    rtrim = rtrim + changeR
    # save to DB
    DB.updateTrimValues(ltrim,rtrim)
    # update robot, commented out when working on remote machine
    # robot.setLeftTrim(ltrim)
    # robot.setRightTrim(rtrim)

    return {'L':ltrim,'R':rtrim}


def changeMotorSpeeds(data):
	# We are given acceleration in x (roll) and y (pitch) and we need to write a controller to command the left and right motor given a combination of these inputs
	#
	# acceptable range of input data:
	#	y:[-100:100]
	#	x:[-100:100]
	#
	# acceptable range for motor commands:
	#	max defined by motor controller: [0:255]
	#	lets constrain that to: [0:200]

	data = json.loads(data)

	y = data['y'];
	if (y > -40 and y < -10):
		y = ( y + 10 ) * ( 200.0 / 30 )
	elif (y > 10 and y < 40):
		y = ( y - 10 ) * ( 200.0 / 30 )
	elif (y > 40):
		y = 100
	elif (y < -40):
		y = -100
	else:
		y = 0

	x = data['x'];
	if (x > -30 and x < -10):
		x = ( x + 10 ) * ( 200.0 / 20 )
	elif (x > 10 and x < 30):
		x = ( x - 10 ) * ( 200.0 / 20 )
	elif (x > 30):
		x = 100
	elif (x < -30):
		x = -100
	else:
		x = 0

	# Left motor -> LM
	# Right motor -> RM

	RM = (y - x) * 0.5
	LM = (y + x) *0.5

	return {'RM':RM,"LM":LM}

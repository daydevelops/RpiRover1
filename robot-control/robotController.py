import json
import time
# import Robot
import sys
sys.path.append('db')
import Logs

def getTrimValues():
    DB = Logs.Logs()
    return DB.getTrimValues()

def initRobot(LEFT_TRIM, RIGHT_TRIM):
    print "initializing robot with l_trim = "+str(LEFT_TRIM)+" and r_trim = "+str(RIGHT_TRIM)
    # robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
    # return robot

def driveRobot(robot,data):
    # DB = Logs.Logs()
    # DB.log('controllerCommands',data)
    motorSpeeds = processInputs(data)
    print ("MC inputs: "+json.dumps(motorSpeeds))
	# robot.leftM(int(motorSpeeds['LM']))
	# robot.rightM(int(motorSpeeds['RM']))

def updateTrim(robot,changeL,changeR):
    DB = Logs.Logs()
    # get trim from db
    trims = getTrimValues()
    ltrim = trims['L']
    rtrim = trims['R']
    # add chagne value
    ltrim = ltrim + changeL
    rtrim = rtrim + changeR
    # save to DB
    DB.updateTrimValues(ltrim,rtrim)
    data = {
        'left_trim':ltrim,
        'right_trim':rtrim
    }
    DB.log('controllerCommands',data)
    # update robot, commented out when working on remote machine
    # robot.setLeftTrim(ltrim)
    # robot.setRightTrim(rtrim)

    return {'L':ltrim,'R':rtrim}


def processInputs(data):
	# acceptable range of input data:
	#	y:[-100:100]
	#	x:[-100:100]
	#
	# acceptable range for motor commands:
	#	max defined by motor controller: [0:255]
	#	lets constrain that to: [0:200]

	# Left motor -> LM
	# Right motor -> RM
	RM = (int(data['speed']) - int(data['heading'])) * 0.5
	LM = (int(data['speed']) + int(data['heading'])) *0.5

	return {'RM':RM,"LM":LM}

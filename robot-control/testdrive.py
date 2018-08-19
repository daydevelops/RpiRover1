import time
import Robot

def initRobot():
    LEFT_TRIM   = 0
    RIGHT_TRIM  = 0

    robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

    robot.leftM(-100)
    time.sleep(2)
    robot.rightM(-100)
    time.sleep(2)
    robot.stop() 


import time
import atexit
import MotorController as MC
class Robot(object):
    def __init__(self, left_trim=0, right_trim=0, stop_at_exit=True):
        """Create an instance of the robot.  Can specify the following optional
        parameters:
         - left_trim: Amount to offset the speed of the left motor, can be positive
                      or negative and use useful for matching the speed of both
                      motors.  Default is 0.
         - right_trim: Amount to offset the speed of the right motor (see above).
         - stop_at_exit: Boolean to indicate if the motors should stop on program
                         exit.  Default is True (highly recommended to keep this
                         value to prevent damage to the bot on program crash!).
        """
        self._left_trim = left_trim
        self._right_trim = right_trim
        self.mc = MC.MotorController() #arduino motor controller class
        # Configure all motors to stop at program exit if desired.
        if stop_at_exit:
            atexit.register(self.stop)
        print "robot initialized"

    def stop(self):
        """Stop all movement."""
        self.mc.stop()
            
    def leftM(self, speed):
        """Spin left motor at given speed"""
        self.mc.rightM(speed)
			
    def rightM(self, speed):
        """Spin right motor at given speed"""
        self.mc.leftM(speed)

    def setLeftTrim(self,trim):
        self._left_trim = trim

    def setRightTrim(self,trim):
        self._right_trim = trim

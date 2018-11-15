# class to interface with motor controller on the arduino 
import serial


class MotorController(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0',9600)

    def stop(self):
        """Stop all movement."""
        print "telling arduino to stop"
        self.ser.write('S;')
            
    def leftM(self, speed):
        """Spin left motor at given speed"""
        print "telling Arduino to change left motor speed"
        print 'L'+str(speed)+';'
        self.ser.write("L"+str(speed)+";")
			
    def rightM(self, speed):
        """Spin right motor at given speed"""
        print "telling Arduino to change right motor speed"
        print 'R'+str(speed)+';'
        self.ser.write('R'+str(speed)+';')



# RpiRover1
Basic raspberry pi rover

## Introduction
This project uses a Flask server with a SocketIO connection between server and client to communicate.

## Next steps:
optimize db logging - too slow

How do I reinitialize the robot if the client comes back from a broken connection?

How do I detect when the client unintentionally leaves the connection? We need to stop the robot when this happens.

When the joystick is let go, send controller output of zero to server

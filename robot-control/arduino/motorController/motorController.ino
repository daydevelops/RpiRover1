#include <string.h>

int enA = 10;
int in1 = 9; 
int in2 = 8;
int in3 = 7;
int in4 = 6;
int enB = 5;

String msg = "";
char command;
int msgReceived = 1;
void setup() {
  pinMode(enA,OUTPUT);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(enB,OUTPUT);
  Serial.begin(9600); // Starts the serial communication
}

void processMessage(char command, String msg) {
  switch (command) {
    case 'L':
      changeLeftMotor(atoi(msg.c_str()));
      break;
    case 'R':
      changeRightMotor(atoi(msg.c_str()));
      break;
    case 'S':
      stopMotors();
      break;
  } 
}

void changeLeftMotor(int speed) {
  Serial.println("changing left");
  Serial.println(speed*2);
}

void changeRightMotor(int speed) {
  Serial.println("changing right");
  Serial.println(speed+1);
}

void stopMotors() {
  Serial.println('Stopping motors');
}

void loop() {
  
  char character; // incoming charcater

  while(Serial.available()) {
      character = Serial.read();
      
      // if this is the start of a new command
      if (msgReceived==1) {
        command = character; // first character is for command type
        msgReceived = 0;
        continue;
      }
      
      if (character == ';') { // end of command
        processMessage(command,msg);
        msg = "";
        msgReceived = 1; // reset
      } else { // character is not the beginning or end of msg
        msg.concat(character);
      }
  }
  
  delay(50);

}

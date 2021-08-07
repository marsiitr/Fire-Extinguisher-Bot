#include <Servo.h>
#include <Math.h>

int servoPin_y = 6;  //for rotation in vertical plane
int servoPin_x = 5;  //for rotation in horizontal plane
int pumpPin = 4;
Servo Servo_y;
Servo Servo_x; 
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  // put your setup code here, to run once:
   Servo_y.attach(servoPin_y);
   Servo_x.attach(servoPin_x);  

   pinMode(pumpPin, OUTPUT);
}

void loop() {
  int counter = 0;
  digitalWrite(pumpPin, HIGH);
  
  float plane_theta=360,z_rotation=360;
  String serialData=Serial.readString(); 
  plane_theta=extractY(serialData);
  z_rotation=extractX(serialData);
  counter = (int)extractZ(serialData);
  delay(100);
  
  
  if(plane_theta < 180 && z_rotation < 180)
  {
    Servo_y.write(round(95+plane_theta)); //mean positions angles adjusted by real world experimentation
    delay(500);
    Servo_x.write(round(100+z_rotation));
    delay(2000);

    if(counter!= 0)
    {
      digitalWrite(pumpPin, HIGH);
      delay(4000);
      digitalWrite(pumpPin, LOW);
      }
    }
}

//buffer string = "X<z_rotation>Y<plane_theta>Z<flame_status>"

int extractX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"),1);
  return data.toFloat();
  }
int extractY(String data){
  data.remove(data.indexOf("Z"));
  data.remove(0,data.indexOf("Y")+1);
  return data.toFloat();
  }
int extractZ(String data){
data.remove(0,data.indexOf("Z")+1);
return data.toFloat();
}

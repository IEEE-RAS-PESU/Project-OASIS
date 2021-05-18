
#define trigPin1 2
#define echoPin1 3

const int motorPin1  = 6;  // Pin 14 of L293
const int motorPin2  = 7;  // Pin 10 of L293


long duration, distance;

void setup()
{
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(motorPin1, OUTPUT);
pinMode(motorPin2, OUTPUT);


}

void loop() {
SonarSensor(trigPin1, echoPin1);
Serial.print(" Distance ");
Serial.println(distance);
 if (distance< 50){
     Serial.println("obstacle present");
       
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    delay(500);
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    delay(500);
    
  }
  else{
    Serial.println("no obstacle");
   
  }
}

void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(1);
digitalWrite(trigPin, HIGH);
delayMicroseconds(5);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;

}
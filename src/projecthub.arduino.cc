//#include <MPU9250.h>
#include <Servo.h>
#include <SR04.h>
 
//PINS FOR ULTRASONICS
#define TRIG_PIN_L  7
#define ECHO_PIN_L  6
#define TRIG_PIN_R  5
#define ECHO_PIN_R  4
 
//PINS FOR COLOR SENSOR
#define s0   8
#define s1   9
#define s2  10
#define s3  11
#define out 12
 
//PIN FOR DIR SERVO
#define SERVO_PIN 3
 
int data = 0; // Data variable used for reading the frequency of colors
int degs;

//Ultrasonic objects
SR04 ul = SR04(ECHO_PIN_L,TRIG_PIN_L);
SR04 ur = SR04(ECHO_PIN_R,TRIG_PIN_R);
 
//Servo object
Servo servo;
 
//MPU object
//MPU9250 mpu;
float yaw;
 
String inputString = "";      // To save what comes from serial
bool stringComplete = false;  // Flag to know if a string received from serial can be evaluated
 
long distance_usl;
long distance_usr;

void setup() {
  Serial.begin(9600);
  inputString.reserve(20);
 
  pinMode(s0,OUTPUT);    //pin modes
  pinMode(s1,OUTPUT);
  pinMode(s2,OUTPUT);
  pinMode(s3,OUTPUT);
  pinMode(out,INPUT);
  digitalWrite(s0,HIGH);  //Putting S0/S1 on HIGH/HIGH levels means the output frequency scalling is at 100%, which is recommended by https://projecthub.arduino.cc/SurtrTech/color-detection-using-tcs3200230-a1e463
  digitalWrite(s1,HIGH);
 
 servo.attach(SERVO_PIN);
  servo.write(70);
 
 
 //Wire.begin();
  delay(2000);
 
  // int connection;
  // do {
  //   connection = mpu.setup(0x68);
  //   Serial.println("Not connected");
  // } while(!connection);
}
// 30 limite derecha
// 130 limite izquierda
void loop() {

  if (stringComplete) {
    inputString.trim(); // To eliminate spaces or line jumps
      degs = inputString.toInt();
      servo.write(degs);
    
    inputString = "";
    stringComplete = false;

  }
  /*
  if (stringComplete) {
    inputString.trim(); // To eliminate spaces or line jumps
 
    //get ultrasonics data
    if (inputString.equalsIgnoreCase("ul")) {
      Serial.println(ul.Distance());
    }
    else if (inputString.equalsIgnoreCase("ur")) {
      Serial.println(ur.Distance());
    }
   
    //get color data
    else if (inputString.equalsIgnoreCase("c")) {
      // The combination of s2 and s3 configure the sensor to be sensitive to a certain kind of light (and so a color), LOW LOW for red, LOW HIGH for green
      // and HIGH HIGH for blue
      digitalWrite(s2,LOW);        
      digitalWrite(s3,LOW);       
      GetColorData();
      Serial.print("-");
     
      digitalWrite(s2,LOW);
      digitalWrite(s3,HIGH);
      GetColorData();
      Serial.print("-");
     
      digitalWrite(s2,HIGH);
      digitalWrite(s3,HIGH);
      GetColorData();
     
      Serial.println();
    }
 
    //get yaw
    else if (inputString.equalsIgnoreCase("y")) {
      Serial.println(yaw, 2);
    }
 
    //set servo angle
    else {

    }
 
    // limpiar para la próxima lectura
    inputString = "";
    stringComplete = false;
   
    // if (mpu.update()) {
    //     static uint32_t prev_ms = millis();
    //     if (millis() > prev_ms + 25) {
    //         yaw = mpu.getYaw();
    //         prev_ms = millis();
    //     }
    // }
  }
*/
// Lectura de ultrasonidos
distance_usl = ul.Distance();
distance_usr = ur.Distance();

// Lectura de colores
digitalWrite(s2, LOW);
digitalWrite(s3, LOW);
int r = pulseIn(out, LOW);

digitalWrite(s2, LOW);
digitalWrite(s3, HIGH);
int g = pulseIn(out, LOW);

digitalWrite(s2, HIGH);
digitalWrite(s3, HIGH);
int b = pulseIn(out, LOW);

// Enviar TODO junto una sola vez
Serial.println(String(distance_usl) + "|" + String(distance_usr) + "|" + String(r) + "|" + String(g) + "|" + String(b));

  delay(59);
}


// This function executes automatically when data comes from serial
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {  // fin de línea
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

void PrintColorData(){
   data=pulseIn(out,LOW);  //We begin timing when out goes LOW and stop when it returns to HIGH, the lower the time, the higher the color wave frequency
   Serial.print(data);
   delay(20);
}

long getStableDistance(SR04 sensor) {
  long d1 = sensor.Distance();
  delay(20);
  long d2 = sensor.Distance();
  delay(20);
  long d3 = sensor.Distance();
  
  // Ordenamos para tomar la MEDIANA (mejor que promedio si hay valores locos)
  long arr[3] = {d1, d2, d3};
  for(int i=0;i<3;i++){
    for(int j=i+1;j<3;j++){
      if(arr[j] < arr[i]){
        long temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr[1]; // valor del medio = mediana
}

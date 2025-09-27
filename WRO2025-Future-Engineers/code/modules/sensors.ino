#include <SR04.h>

//PINS FOR ULTRASONICS (F: Front, B: Back, LF: Left Front, LB: Left Back, RF: Right Front, RB: Right Back)
#define TRIG_PIN_F  3
#define ECHO_PIN_F  2
#define TRIG_PIN_B  4
#define ECHO_PIN_B  5
#define TRIG_PIN_LF 2  //IMPORTANT NOTE: For now the pins are repeated because only two ultrasonic sensores are being tested
#define ECHO_PIN_LF 3
#define TRIG_PIN_LB 2
#define ECHO_PIN_LB 3
#define TRIG_PIN_RF 2
#define ECHO_PIN_RF 3
#define TRIG_PIN_RB 2
#define ECHO_PIN_RB 3

//PINS FOR COLOR SENSOR
#define s0   8
#define s1   9
#define s2  10
#define s3  11
#define out 12

int data = 0; // Data variable used for reading the frequency of colors

//Ultrasonic objects
SR04 uf = SR04(ECHO_PIN_F,TRIG_PIN_F);
SR04 ub = SR04(ECHO_PIN_B,TRIG_PIN_B);
//SR04 ulf = SR04(ECHO_PIN_LF,TRIG_PIN_LF);
//SR04 u1b = SR04(ECHO_PIN_LB,TRIG_PIN_LB);
//SR04 urf = SR04(ECHO_PIN_RF,TRIG_PIN_RF);
//SR04 urb = SR04(ECHO_PIN_RB,TRIG_PIN_RB);

String inputString = "";      // To save what comes from serial
bool stringComplete = false;  // Flag to know if a string received from serial can be evaluated

void setup() {
  Serial.begin(115200);
  inputString.reserve(20);

  pinMode(s0,OUTPUT);    //pin modes
  pinMode(s1,OUTPUT);
  pinMode(s2,OUTPUT);
  pinMode(s3,OUTPUT);
  pinMode(out,INPUT);
  digitalWrite(s0,HIGH);  //Putting S0/S1 on HIGH/HIGH levels means the output frequency scalling is at 100%, which is recommended by https://projecthub.arduino.cc/SurtrTech/color-detection-using-tcs3200230-a1e463
  digitalWrite(s1,HIGH);
}

void loop() {
  if (stringComplete) {
    inputString.trim(); // To eliminate spaces or line jumps

    if (inputString.equalsIgnoreCase("uf")) {
      Serial.println(uf.Distance());
    }
    if (inputString.equalsIgnoreCase("ub")) {
      Serial.println(ub.Distance());
    }
    if (inputString.equalsIgnoreCase("ulf")) {
      //Serial.println(ulf.Distance());
    }
    if (inputString.equalsIgnoreCase("ulb")) {
      //Serial.println(ulb.Distance());
    }
    if (inputString.equalsIgnoreCase("urf")) {
      //Serial.println(urf.Distance());
    }
    if (inputString.equalsIgnoreCase("urb")) {
      //Serial.println(urb.Distance());
    }
    
    else if (inputString.equalsIgnoreCase("c")) {
      digitalWrite(s2,LOW);        // The combination of s2 and s3 configure the sensor to be sensitive to a certain kind of light (and so a color), LOW LOW for red, LOW HIGH for green
      digitalWrite(s3,LOW);        // and HIGH HIGH for blue
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

    // limpiar para la próxima lectura
    inputString = "";
    stringComplete = false;
  }
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

void GetColorData(){
   data=pulseIn(out,LOW);  //We begin timing when out goes LOW and stop when it returns to HIGH, the lower the time, the higher the color wave frequency
   Serial.print(data);
   delay(20);
}

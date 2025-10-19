# WRO Repository TEAM Astro
## Team Information

<p align="center">
  <img width="400" height="400" alt="logo 2" src="https://github.com/user-attachments/assets/ba2f4f4b-e1bd-4858-845c-bd96b7c35279" />
</p>

📜 Documenter: Renso Isael Peralta Ureña (Right)

🧑‍🔧 Programmer: José Miguel Comprés Arias (Left)

🧑‍🔧 Mechanic: Yoel Samuel Castillo Castillo (Front)

![team photo](https://github.com/user-attachments/assets/d0d88cb5-2361-492b-bfa1-58ac8055714e)

PUCMM, Dominican Republic <img width="15" height="15" alt="image" src="https://github.com/user-attachments/assets/cacb6bc7-76ba-49e5-9df6-87c6d36aa328" />

## Content Organization

This repository contains the complete documentation and resources for our autonomous vehicle designed for the WRO 2025 Future Engineers category from ASTRO team.

### Repository Structure

* **`t-photos`** - Contains 2 photos of the team:
  * Official team photo with all members
  * Funny/casual photo with all team members

* **`v-photos`** - Contains 6 photos of the vehicle showcasing:
  * Front view
  * Back view
  * Left side view
  * Right side view
  * Top view
  * Bottom view

* **`videos`** - Contains `video.md` file with links to driving demonstration videos including:
  * Tests carried out

* **`schemes`** - Contains electromechanical schematic diagrams (JPEG/PNG/PDF form``at) illustrating:
  *En proceso todavia*

* **`src`** - Contains the control software source code:
  *En proceso todavia*

* **`models`** - Contains 3D models and design files:
  * STL files for 3D-printed parts.
  * First prototype design files.
  * Second prototype design files (optimized version).

## Introduction
This project presents our autonomous vehicle designed for the 2025 World Robot Olympiad (WRO) competition in the Future Engineers category. The robot is fully autonomous, capable of navigating a closed course, detecting and avoiding objects.

AUTONOMOUS NAVIGATION ROBOT

## Project Overview
This repository contains all the technical documentation, code, and design files for our autonomous navigation robot developed for the WRO Future Engineers. Our project focuses on creating a practical and efficient self-driving vehicle capable of navigating complex environments using sensor fusion and intelligent decision-making algorithms.

## Models

### Main components
- **Main Controller**: Raspberry Pi 5 (high-level processing)
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/685aa0d4-bf54-4382-9f8d-9cf324937124" />

[Link to buy the raspberry pi 5](https://www.amazon.com/-/es/SC1112-Raspberry-Pi-5-8GB/dp/B0CK2FCG1K/ref=sr_1_3_mod_primary_new?sr=8-3)

- **Real-time Controller**: Arduino UNO R3
<img width="400" height="" alt="image" src="https://github.com/user-attachments/assets/24b10c39-544b-4a5b-ac41-419f63239714" />

[Link to buy the arduino UNO R3](https://www.amazon.com/-/es/Arduino-Uno-R3-Microcontrolador-A000066/dp/B008GRTSV6/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-1)

- **Interface Board**: Robot Hat v4
<img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/3f94f7af-df98-439d-bea3-c3194a26fa7b" />

[Link to buy Robot Hat v4](https://www.amazon.com/-/es/SunFounder-expansi%C3%B3n-Raspberry-conductores-recargable/dp/B0CKTD7QJB)

- **Sensors**:
  - 2x Ultrasonic sensors HCSR04 (Bilateral coverage)
  
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/590916af-7b44-45c0-85b3-133d8bbc135b" />

  [Link to buy ultrasonic sensors HCSR04](https://www.amazon.com/-/es/DIYables-ultras%C3%B3nico-HC-SR04-Arduino-Raspberry/dp/B0BDFLPZ2R/ref=sr_1_14?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-14)

  - 1x Color sensor TCS 3200 (line detection)
  
  <img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/d89a39e0-f70a-46fc-9dfa-999278ceed20" />

  [Link to buy Color Sensor TCS 3200](https://www.amazon.com/-/es/Teyleten-TCS3200-TCS230-reconocimiento-Arduino/dp/B08HH8QYF8/ref=sr_1_2?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-2)

  - 1x IMU MPU-9250 (orientation)
  
  <img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/0a14f562-5c5b-47a6-8f5e-9692b0a819a5" />

  [Link to buy IMU MPU-9250](https://www.amazon.com/-/es/giroscopio-magn%C3%A9tico-aceleraci%C3%B3n-acelerador-magnet%C3%B3metro/dp/B01I1J0Z7Y/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-1)
 
  - 1x Raspberry Pi Camera (computer vision)
  
  <img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/cf31cf94-6689-4a6c-8263-90a4608be925" />

  [Link to buy Raspberry Pi Camera](https://www.amazon.com/-/es/Arducam-peque%C3%B1o-megapixeles-pixeles-Raspberry/dp/B012V1HEP4/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-1)

- **Motors**: TT Motor x1
  
  <img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/5c7384f9-a6d9-488a-8b4a-adbc57c7ab80" />

  [Link to buy TT Motor](https://www.amazon.com/-/es/Diann-unids-Motor-cambios-200RPM/dp/B0BR7S2TRY/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-5)

- **Power Source**: Battery
  
  <img width="600" height="392" alt="image" src="https://github.com/user-attachments/assets/dab5331b-5598-41fc-affd-9bf23f97e514" />

  [Link to buy Battery](https://www.indiamart.com/proddetail/5v-li-ion-battery-22444168691.html)


## First Prototype Design

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/3b4e8dc8-8090-4ecc-8f10-5860a87f4374" />

Our initial chassis design was conceived with a compact, enclosed structure that prioritized sensor integration and component protection. The first prototype incorporated the following design elements:

*Sensor Layout*:
The chassis featured mounting positions for four ultrasonic sensors strategically distributed to provide comprehensive obstacle detection coverage around the vehicle's perimeter.

*Camera Integration*:
A dedicated frontal mounting space was designed to house the Raspberry Pi Camera module, positioned to provide an optimal field of view for computer vision and object detection tasks.

*Internal Electronics Compartment*:
The original design included an enclosed internal cavity intended to house all electronic components, including the Raspberry Pi 5, Robot Hat v4, Arduino, sensors, and wiring. This approach aimed to protect the electronics from external interference and provide a clean, organized appearance.

*Motor Placement*:
A designated space was allocated for the DC motor; however, the initial design lacked detailed consideration for motor mounting mechanics, power transmission, and drivetrain integration.

*Critical Design Oversight*:
During the physical assembly phase, we encountered a significant spatial constraint that was not apparent in the CAD model. The combined height of the Raspberry Pi 5 board and the Robot Hat v4 interface board exceeded the available vertical clearance within the internal compartment. We had not physically measured these stacked components during the design phase, assuming the CAD dimensions would accommodate them.

*Consequence*: The electronics could not fit inside the chassis as originally planned.

*Immediate Solution*: We repositioned the Raspberry Pi 5 and Robot Hat v4 assembly on top of the chassis structure, securing them with standoffs and mounting brackets. While this modification solved the spatial issue and improved heat dissipation and accessibility, it exposed the electronics to potential impacts and increased the vehicle's center of gravity.

Motor Integration Challenge:
Similarly, the motor mounting system was insufficiently detailed in the first prototype. The lack of proper motor brackets, shaft alignment considerations, and drivetrain coupling mechanisms became evident during assembly.

Resolution: This oversight necessitated a complete chassis redesign to properly integrate the motor system, optimize weight distribution, and ensure reliable power transmission to the wheels.

This experience highlighted the critical importance of:

*Physical measurement and test-fitting of components before finalizing CAD designs
Accounting for tolerance stack-up and assembly clearances
Detailed planning of mechanical subsystems (motor mounts, drivetrain, wiring routes)
Iterative prototyping to validate design assumptions*

These challenges directly informed the development of our second prototype, which addressed all identified spatial and mechanical integration issues.

## Second Prototype Design

After evaluating the limitations of our first prototype, we decided to completely redesign the chassis to optimize sensor positioning and improve overall functionality. Building on lessons learned, we planned to incorporate five ultrasonic sensors for enhanced environmental awareness.

Ultrasonic Sensor Holder Design

<img width="608" height="246" alt="chasis largo" src="https://github.com/user-attachments/assets/1977c2ee-f1ab-4214-951c-4f69846def59" />

We designed a dedicated ultrasonic sensor holder to accommodate the five sensors we intended to use: two positioned at the front for forward obstacle detection, one at the rear for reverse awareness, and two mounted mid-chassis for lateral coverage. While this configuration seemed optimal in theory, practical testing revealed a critical flaw—the two front-mounted sensors created physical interference with the front wheel assembly during steering maneuvers, necessitating their removal from the chassis.

Front Wheel Support Structure

<img width="200" height="200" alt="soporte rueda" src="https://github.com/user-attachments/assets/fea2f472-2f9c-48e3-ba95-0378646b812f" />

Unlike the first design, the second prototype featured an improved front wheel support system. This component served a dual purpose: securely mounting the wheel assembly while providing a stable connection point to the vehicle's outer cover. The redesigned support improved structural rigidity and simplified the assembly process.

<img width="200" height="200" alt="segundo soporte ruedas" src="https://github.com/user-attachments/assets/bb8ba79f-5925-48d6-8951-4cd918968b57" />

Second Prototype Assembly Views

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/ba5936a6-692e-4b4e-a551-59d259048d1d" />

🔧 Challenges and Solutions During Final Design

During the development and assembly of our autonomous vehicle, we encountered several technical challenges that required creative solutions and design modifications. These challenges taught us valuable lessons about iterative design and practical engineering problem-solving.

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/b5808995-2f03-4338-a36a-282f4b9e5cf4" />

Dimensional Compliance: Reducing Vehicle Length

Critical Constraint: Competition regulations required vehicles to not exceed specific dimensional limits. Our second prototype measured 11.8 inches in length, exceeding the maximum allowed dimension by one full inch.

Problem: The chassis design, while functionally sound, was too long to comply with competition rules. The extended length was primarily due to:

The frontal sensor mounting structure extending beyond necessary limits
The battery holder positioned too far forward
Overall chassis design that prioritized component spacing over compactness

Solution - Comprehensive Chassis Modification:
We implemented a series of strategic modifications to reduce the vehicle's footprint:

Front Section Reduction: We cut and removed approximately one inch from the front portion of the chassis, eliminating excess material while maintaining structural integrity for the camera mount and essential frontal components.

Color Sensor Relocation: Instead of mounting the TCS 3200 color sensor externally on the front surface, we created a custom opening on the underside (bottom) of the chassis. This modification allowed us to recess the sensor into the chassis body, positioning it closer to the ground for optimal line detection while recovering valuable frontal space.

Battery Holder Repositioning: We recessed the battery mounting bracket deeper into the chassis cavity, moving it further back from the front edge. This change not only reduced overall length but also improved weight distribution by centering the battery mass.

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/34787083-5dad-4437-b0b3-238b8af1a8ce" />

Ultrasonic Sensor Reduction: To accommodate the shortened chassis and address other constraints (detailed below), we removed three ultrasonic sensors from the design, further simplifying the frontal structure.

Result: These combined modifications successfully reduced the vehicle length from 11.8 inches to 10.8 inches, achieving full compliance with competition regulations while maintaining all essential functionality.
Arduino Pin Limitations and Sensor Reduction
Problem: Our initial plan to use five ultrasonic sensors, combined with the color sensor, IMU, camera interface, servo motor, and DC motor driver, exceeded the available GPIO pins on the Arduino UNO R3. Each ultrasonic sensor requires two digital pins (trigger and echo), meaning five sensors would consume 10 pins alone, leaving insufficient pins for other critical components.
Solution: We strategically reduced the ultrasonic sensor count from five to two, retaining only the most essential sensors for navigation:

One front-facing sensor for primary obstacle detection
One side-mounted sensor for wall-following and lateral awareness

This reduction freed up six digital pins (3 sensors × 2 pins each), allowing all remaining components to be properly connected without requiring a larger microcontroller.
Ultrasonic Sensor Interface Selection: Raspberry Pi vs. Arduino
Problem: During initial testing, we attempted to interface the ultrasonic sensors directly with the Raspberry Pi 5 GPIO pins. However, we encountered persistent issues with unreliable distance readings and inconsistent sensor response times. The problem stemmed from the Raspberry Pi's non-real-time operating system (Linux), which cannot guarantee precise microsecond-level timing required for accurate ultrasonic echo pulse measurement.
Solution: We decided to connect the ultrasonic sensors to the Arduino UNO R3 instead of the Raspberry Pi. The Arduino's real-time microcontroller architecture provides deterministic timing, ensuring accurate pulse duration measurements. The Arduino reads the sensor data and transmits processed distance values to the Raspberry Pi via serial communication (UART) through the Robot Hat v4 interface.
Technical Justification:

Arduino UNO R3: Real-time operation with precise microsecond timing for reliable ultrasonic measurements
Raspberry Pi 5: Handles higher-level processing (computer vision, navigation logic, decision-making) without timing-critical sensor interfacing

This division of responsibilities between the two processors optimized system reliability and performance.
Color Sensor Integration
One of the first challenges we faced was fitting the color sensor into its designated mounting space. The original CAD design did not account for the actual physical dimensions and connector orientation of the TCS 3200 color sensor module.
Problem: The color sensor module, including its I2C connector pins, exceeded the allocated space in the front sensor mount structure. The rigid PCB design prevented us from repositioning it without structural modifications.
Solution: We used a soldering iron to carefully create a custom opening in the bottom of the plastic chassis. This allowed us to recess the sensor body while keeping the optical window at the optimal height and angle for line detection. The modification maintained the sensor's downward-facing orientation (approximately 30-45° angle) necessary for accurate color detection of the track surface while minimizing ambient light interference.
Result: The color sensor was successfully integrated and provided reliable line detection throughout testing while contributing to the overall length reduction of the chassis.
Rear Wheel Support Structure Failure
Problem: The 3D-printed rear wheel support arms, designed to hold rubber tires in place, experienced structural failure during initial testing. The stress concentration points where the tires connected to the motor shafts caused the plastic supports to crack and eventually break. This was likely due to:

Insufficient wall thickness in the 3D-printed part
Vibrations from the DC motors during operation
Lateral forces during turning maneuvers

Solution: Unable to quickly redesign and reprint the support structure, we implemented an emergency repair using a soldering iron technique:

We carefully heated the soldering iron to a temperature suitable for melting PLA/ABS plastic
We repositioned the broken rubber tire holders against the motor mounting arms
We used the soldering iron tip to "weld" the plastic pieces together, creating a reinforced joint
We added additional plastic material where needed to strengthen critical stress points

Result: This field repair successfully restored structural integrity and proved durable enough for the remainder of our testing and competition preparation. However, this experience highlighted the importance of stress testing 3D-printed components and designing with appropriate safety margins for dynamic loads.
Microcontroller Selection Optimization
Our electronic architecture underwent a significant simplification during the final assembly phase.
Original Plan: Arduino Mega 2560

Reason for selection: The Mega provides 54 digital I/O pins and 16 analog inputs, which we initially believed necessary to accommodate multiple ultrasonic sensors, the color sensor (I2C), the IMU (I2C), servo motors (PWM pins), and the DC motor driver.

Modified Implementation: Arduino UNO R3

Reason for change: After reducing the ultrasonic sensor count to two, the total pin requirement decreased significantly:

2 ultrasonic sensors: 4 digital pins (2 trigger + 2 echo)
Color sensor: I2C bus (SDA/SCL) - 2 pins
IMU: I2C bus (shared) - 0 additional pins
Servo motor (steering): 1 PWM pin
DC motor driver: 2-4 digital pins
Total: approximately 9-11 pins

The Arduino UNO R3 provides 14 digital I/O pins and 6 analog inputs, which is more than sufficient for our reduced configuration. This change offered several advantages:

Reduced physical footprint: The Uno is smaller and lighter than the Mega
Improved space utilization: Easier to fit within the compact chassis
Cost optimization: Lower component cost without sacrificing functionality
Simplified wiring: Fewer unused pins reduced wiring complexity
Real-time sensor reliability: Better ultrasonic sensor performance compared to Raspberry Pi GPIO

Power Distribution Solution
Managing multiple 5V power connections for sensors and modules with limited power pins on the Arduino.
Solution: We implemented a breadboard-based power distribution system:

Positive rail (5V): Connected to Arduino's 5V output pin
Ground rail (0V/GND): Connected to Arduino's GND pin
Connected devices: All sensors requiring 5V power (ultrasonic sensors, color sensor) were connected to the breadboard rails

Advantages:

Organized and accessible power distribution
Easy troubleshooting and component replacement
Reduced stress on Arduino's voltage regulator by distributing current load
Clean cable management

## Sources (src)

File: projecthub.arduino.cc

## What does this code do?

This code controls an Arduino robot that can:
- **Detect distances** to the left and right using ultrasonic sensors
- **Identify colors** using a TCS3200/230 sensor
- **Rotate** using a servo motor
- **Communicate** with a computer via serial port

## Hardware Connections

### Left Ultrasonic Sensor:
- `TRIG` → Pin 7
- `ECHO` → Pin 6
- `VCC` → 5V
- `GND` → GND

### Right Ultrasonic Sensor:
- `TRIG` → Pin 5
- `ECHO` → Pin 4
- `VCC` → 5V
- `GND` → GND

### TCS3200 Color Sensor:
- `S0` → Pin 8
- `S1` → Pin 9
- `S2` → Pin 10
- `S3` → Pin 11
- `OUT` → Pin 12
- `VCC` → 5V
- `GND` → GND

### Servo Motor:
- Signal Wire → Pin 3
- Red Wire → 5V
- Brown/Black Wire → GND

## 📚 Required Libraries

Before uploading the code, install these Libraries:

```cpp
#include <Servo.h> // To control the servo
#include <SR04.h> // For ultrasonic sensors
```

**Installation:** In the Arduino IDE, go to `Tools > Manage Libraries` and search for these libraries.

## Step-by-Step Code Explanation

### 1. Pin Definitions

```cpp
// ULTRASONIC PINS
#define TRIG_PIN_L 7 // Left sensor trigger pin
#define ECHO_PIN_L 6 // Left sensor echo pin
#define TRIG_PIN_R 5 // Right sensor trigger pin
#define ECHO_PIN_R 4 // Right sensor echo pin

// COLOR SENSOR PINS
#define s0 8 // Frequency setting
#define s1 9 // Frequency setting
#define s2 10 // Color filter selection
#define s3 11 // Color filter selection
#define out 12 // Frequency output

// SERVO PIN
#define SERVO_PIN 3 // Servo control pin
```

### 2. Variables globals

```cpp
int data = 0; // Stores the color frequency
int degs; // Degrees for the servo
long distance_usl; // Left sensor distance
long distance_usr; // Right sensor distance
```

### 3. Object Creation

```cpp
SR04 ul = SR04(ECHO_PIN_L, TRIG_PIN_L); // Left ultrasonic sensor
SR04 ur = SR04(ECHO_PIN_R, TRIG_PIN_R); // Right ultrasonic sensor
Servo servo; // Servo object
```

### 4. Initial Setup

```cpp
void setup() {
Serial.begin(9600); // Start serial communication

// Configure color sensor pins
pinMode(s0, OUTPUT);
pinMode(s1, OUTPUT);
pinMode(s2,OUTPUT);
pinMode(s3,OUTPUT);
pinMode(out,INPUT);

// Sets frequency to 100% (maximum precision)
digitalWrite(s0,HIGH);
digitalWrite(s1,HIGH);

// Starts servo in center position (70°)
servo.attach(SERVO_PIN);
servo.write(70);

delay(2000); // Waits 2 seconds to stabilize
}
```

### 5. Main Loop

The code performs the following operations continuously:

#### a) Servo control via serial
```cpp
if (stringComplete) {
inputString.trim(); // Clears spaces
degs = inputString.toInt(); // Converts text to numbers
servo.write(degs); // Move the servo
inputString = "";
stringComplete = false;
}
```

**Servo limits:**
- Right: 30°
- Left: 130°
- Center: ~70-80°

#### b) Reading ultrasonic sensors
```cpp
distance_usl = ul.Distance(); // Left distance in cm
distance_usr = ur.Distance(); // Right distance in cm
```

#### c) Reading the color sensor

The sensor detects the RGB components of the reflected light:

```cpp
// Detect RED
digitalWrite(s2, LOW);
digitalWrite(s3, LOW);
int r = pulseIn(out, LOW);

// Detect GREEN
digitalWrite(s2, LOW);
digitalWrite(s3, HIGH);
int g = pulseIn(out, LOW);

// Detect BLUE
digitalWrite(s2, HIGH);
digitalWrite(s3, HIGH);
int b = pulseIn(out, LOW);
```

**How ​​does it work?**
- S2/S3 combinations select which color to detect
- `pulseIn` measures the pulse time (shorter time = greater color intensity)

#### d) Sending data
```cpp
Serial.println(String(distance_usl) + "|" + String(distance_usr) + "|" +
String(r) + "|" + String(g) + "|" + String(b));
```

Output format: `distance_left|distance_right|red|green|blue`

### 6. Receiving serial commands

```cpp
void serialEvent() {
while (Serial.available()) {
char inChar = (char)Serial.read();
if (inChar == '\n') {
stringComplete = true; // Mark the command complete
} else {
inputString += inChar; // Construct the command
}
}
}
```

This function is executed automatically when data arrives via serial.

## Code: bottom.py

This Python script creates a simple button-controlled system that:

Monitors a button for press events
Controls an LED to indicate button state
Launches another Python script when the button is pressed
Prevents accidental multiple triggers with debouncing

This is perfect for robots or projects where you need a physical button to start a specific program or routine.

## Required Libraries
This project uses the robot_hat library, which is typically included with SunFounder robot kits:
bash# If not already installed:
pip3 install robot-hat
🔌 Hardware Connections
Button Connection:

One side → GPIO25 (labeled as "SW" on some boards)
Other side → GND
Internal pull-up resistor enabled (no external resistor needed)

LED Connection:

LED anode (long leg) → GPIO26 through 220Ω resistor
LED cathode (short leg) → GND

Circuit Diagram:
GPIO25 (SW) ----[BUTTON]---- GND

GPIO26 ----[220Ω]----[LED]---- GND
              +         -
Code Explanation - Line by Line

1. Import Required Libraries
pythonfrom robot_hat import Pin
import time
import os

robot_hat: Provides easy GPIO control for Raspberry Pi
time: For delays and preventing button bounce
os: To execute system commands (run other scripts)

2. Hardware Setup
pythonbutton = Pin("SW", Pin.IN, Pin.PULL_UP)   # Button USR (GPIO25)
led = Pin(26, Pin.OUT)                    # LED (GPIO26)
Button Configuration:

"SW": Special label for GPIO25 (user switch)
Pin.IN: Sets pin as input
Pin.PULL_UP: Enables internal pull-up resistor

Button reads HIGH (1) when not pressed
Button reads LOW (0) when pressed

LED Configuration:

26: GPIO pin number
Pin.OUT: Sets pin as output

3. Define Script Path
python# Path to the file you want to execute
script_path = "/home/admin/Documents/pruebaAbierta1.py"
This is the full path to the Python script that will run when the button is pressed.
Important: Update this path to match your script location

5. Initial LED State
pythonled.on()
Turns on the LED when the program starts, indicating the system is ready.
6. Main Control Loop
pythonwhile True:
    if button.value() == 1:  # Pressed
        led.on()
        os.system(f"python3 {script_path}")  # Execute the other script
        time.sleep(0.5)  # Avoid repetition due to bounce
    else:
        led.off()
    time.sleep(0.1)
Loop Behavior:

Button Check: button.value() returns:

1 when button is pressed (connected to ground)
0 when button is not pressed (pulled high)

When Button is Pressed:

LED turns ON
External script executes using os.system()
0.5 second delay prevents multiple triggers (debouncing)

When Button is Released:

LED turns OFF

Loop Delay:

0.1 second delay reduces CPU usage
Provides responsive button checking (~10 checks per second)

## How to Use This Code
Step 1: Setup Your Hardware

Connect the button to GPIO25 and GND
Connect the LED to GPIO26 (with resistor) and GND
Power up your Raspberry Pi

Step 2: Prepare Your Scripts

Save this launcher script (e.g., as button_launcher.py)
Create or locate the script you want to launch
Update the script_path variable with the correct path

Step 3: Run the Launcher
bashpython3 button_launcher.py
Step 4: Test the System

Press the button → LED lights up and your script runs
Release the button → LED turns off
The launcher continues running, ready for the next press

## Use Cases
This button launcher is perfect for:

Robot startup sequences - Press to begin autonomous navigation
Data collection triggers - Start sensor logging on demand
Mode switching - Toggle between different robot behaviors
Emergency stops - Launch shutdown or safe mode scripts
Demo activation - Start presentation routines

## Code: openChallenge.py

This Python script creates an autonomous robot that:
- **Navigates using ultrasonic sensors** (left and right distance detection)
- **Adjusts steering automatically** based on sensor readings
- **Captures video feed** from a Raspberry Pi camera
- **Detects colored lines** for navigation markers (using RGB sensor)
- **Communicates with Arduino** via serial for sensor data and servo control

The robot uses a wall-following algorithm to navigate corridors or paths while avoiding obstacles.

### Software Requirements:
```bash
# Install required Python packages
pip3 install pyserial
pip3 install opencv-python
pip3 install picamera2
# Astro library (specific to robot kit)
```

## System Architecture

```

┌─────────────┐     Serial      ┌─────────────┐
│  Raspberry  │◄──────────────► │   Arduino   │
│     Pi      │    /dev/ttyACM0 │             │
└──────┬──────┘                 └──────┬──────┘
       │                                │
   ┌───┴───┐                     ┌─────┴─────┐
   │  HAT  │                     │  Sensors  │
   └───┬───┘                     │  & Servo  │
       │                         └───────────┘
   ┌───┴───┐
   │ Motor │
   └───────┘

```

## Key Parameters and Constants

```python
SERIAL_PORT = "/dev/ttyACM0"  # Arduino serial connection
BAUD_RATE   = 9600            # Serial communication speed

DISCR_DIST  = 3               # Distance threshold (unused in current version)
REDIR_ANGLE = 40              # Redirection angle for turns
CENTER = 70                   # Servo center position (degrees)
MAX_ANGLE = 40                # Maximum steering angle from center
```

### Servo Limits:
- **Minimum angle**: CENTER - MAX_ANGLE = 30°
- **Maximum angle**: CENTER + MAX_ANGLE = 110°
- **Center/Straight**: 70°

##  Code Explanation - Section by Section

### 1. Imports and Setup

```python
from astro import Astro      # Robot control library
import serial                # Arduino communication
import time                  # Delays and timing
import cv2                   # Image processing
from picamera2 import Picamera2  # Camera interface
```

### 2. Camera Initialization

```python
picam2 = Picamera2()

# Configure camera resolution
config = picam2.create_preview_configuration({"size": (640, 480)})
picam2.configure(config)

picam2.start()
time.sleep(0.2)  # Allow camera to stabilize
```

The camera runs at 640x480 resolution for a balance between quality and performance.

### 3. Helper Functions

#### Constrain Function
```python
def constrain(x, mn, mx):
    return max(mn, min(mx, x))
```
Limits a value between minimum and maximum bounds (used for servo angles).

#### Serial Communication
```python
def sensor_comm(command):
    ser.write((command + "\n").encode('utf-8'))
```
Sends commands to Arduino (primarily servo angle values).

### 4. Data Reading Functions

The code includes three versions of the data reading function, with `leer_datos3` being the most robust:

```python
def leer_datos3(timeout_seconds=1.0):
    start = time.time()
    
    while True:
        linea = ser.readline().decode(errors="ignore").strip()
        
        # Timeout check
        if not linea:
            if time.time() - start > timeout_seconds:
                raise ValueError("Timeout: no data received")
            continue
        
        # Format validation
        if "|" not in linea:
            if time.time() - start > timeout_seconds:
                raise ValueError(f"Malformed line: {linea!r}")
            continue
        
        # Parse data
        partes = linea.split("|")
        
        # Pad missing values with zeros
        while len(partes) < 5:
            partes.append("0")
        
        # Extract values
        usl_str, usr_str, r_str, g_str, b_str = partes[:5]
        
        try:
            usl = float(usl_str)  # Left ultrasonic
            usr = float(usr_str)  # Right ultrasonic
            r = float(r_str)      # Red component
            g = float(g_str)      # Green component
            b = float(b_str)      # Blue component
            return usl, usr, r, g, b
        except ValueError:
            if time.time() - start > timeout_seconds:
                raise
            continue
```

**Data Format**: `left_distance|right_distance|red|green|blue`

### 5. Main Navigation Loop

```python
# Initialize robot
bot = Astro()
line_count = 0

bot.stop()
time.sleep(5)  # Wait before starting

# Get initial sensor sum
left_dist, right_dist, r, g, b = leer_datos3()
Sum_Initial = left_dist + right_dist

while True:
    # Move forward
    bot.forward(90)  # Speed: 90
    
    # Read sensors
    left_dist, right_dist, r, g, b = leer_datos3()
    
    # Capture and display camera image
    img = picam2.capture_array()
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("CSI Camera (Picamera2 -> OpenCV)", img_bgr)
    
    # Calculate current sum
    Sum_Temp = left_dist + right_dist
    
    # Navigation algorithm
    if(Sum_Temp - 10 < Sum_Initial):
        # Walls closing in - adjust based on difference
        angle = CENTER + float(left_dist - right_dist) * (float(MAX_ANGLE) / 30)
        sensor_comm(str(constrain(angle, CENTER - MAX_ANGLE, CENTER + MAX_ANGLE)))
        
    elif(Sum_Temp - 10 > Sum_Initial):
        # Walls opening up - adjust based on sum
        angle = CENTER + float(left_dist + right_dist) * (float(MAX_ANGLE) / 30)
        sensor_comm(str(constrain(angle, CENTER - MAX_ANGLE, CENTER + MAX_ANGLE)))
        
    else:
        # Maintain center
        sensor_comm("70")
```

### 6. Navigation Algorithm Explained

The robot uses a **corridor-following algorithm**:

1. **Initial Calibration**: Records the sum of left and right distances at start
2. **Continuous Monitoring**: Compares current sum with initial sum
3. **Steering Decisions**:
   - **Walls closing in** (Sum_Temp < Sum_Initial - 10):
     - Steers based on the difference between sensors
     - Moves away from the closer wall
   - **Walls opening up** (Sum_Temp > Sum_Initial + 10):
     - Uses the sum of distances for steering
     - Helps navigate open areas
   - **Normal corridor**: Maintains center position

### 7. Alternative Navigation Code (Commented Out)

The code includes an alternative navigation method:

```python
# Smooth out noisy readings
real_l = left_dist
if (abs(last_l - left_dist) > 10):
    real_l = last_l  # Use last value if change too large

# Different steering sensitivity based on distance difference
if abs(left_dist - right_dist < 40):
    # Normal steering
    angle = CENTER + float(real_l - real_r) * (float(MAX_ANGLE) / 20)
else:
    # More aggressive steering for larger differences
    angle = CENTER + float(real_l - real_r) * (float(50) / 20)

# Line detection for counting laps/sections
if min(r, min(g, b)) == r and r < min(g, b):
    line_count += 1  # Red line detected
```

### 8. Error Handling

```python
try:
    # Main code
except serial.SerialException as e:
    print(f"ERROR opening port: {e}")
except KeyboardInterrupt:
    print("\nReading stopped by user.")
finally:
    # Cleanup
    if 'ser' in locals() and ser.is_open:
        ser.close()
    picam2.stop()
    cv2.destroyAllWindows()
```

## How to Use This Code

### Step 1: Hardware Setup
1. Connect Arduino to Raspberry Pi via USB
2. Upload the Arduino sensor code (from previous tutorial)
3. Mount ultrasonic sensors pointing left and right
4. Connect camera to CSI port
5. Ensure robot wheels and servo are properly connected

### Step 2: Software Configuration
1. Find Arduino port:
   ```bash
   ls /dev/tty*  # Look for /dev/ttyACM0 or /dev/ttyUSB0
   ```
2. Update `SERIAL_PORT` if different
3. Install required libraries

### Step 3: Run the Robot
```bash
python3 autonomous_robot.py
```

### Step 4: Monitor Operation
- Camera feed window shows real-time view
- Terminal displays sensor readings
- Press `Ctrl+C` to stop safely

## Understanding the Output

### Terminal Output:
```
RAW: 15|20|150|200|180
Distancia izquierda: 15.0
Distancia derecha: 20.0
Sumatoria Inicial: 35.0
Sumatoria: 35.0
```

- **RAW**: Raw serial data from Arduino
- **Distance values**: In centimeters
- **Sum values**: Used for navigation decisions

## 🔧 Tuning and Optimization

### 1. Steering Sensitivity
```python
# Current formula: MAX_ANGLE / 30
# Increase divisor for less sensitive steering
angle = CENTER + float(left_dist - right_dist) * (float(MAX_ANGLE) / 30)

# More sensitive (faster reactions)
angle = CENTER + float(left_dist - right_dist) * (float(MAX_ANGLE) / 20)

# Less sensitive (smoother movement)
angle = CENTER + float(left_dist - right_dist) * (float(MAX_ANGLE) / 40)
```

### 2. Speed Control
```python
# Current: constant speed
bot.forward(90)

# Dynamic speed based on obstacles
if min(left_dist, right_dist) < 15:
    bot.forward(60)  # Slow down near walls
else:
    bot.forward(90)  # Normal speed
```

### 3. Wall Detection Threshold
```python
# Current: 10cm buffer
if(Sum_Temp - 10 < Sum_Initial):

# More sensitive to changes
if(Sum_Temp - 5 < Sum_Initial):

# Less sensitive (for wider corridors)
if(Sum_Temp - 15 < Sum_Initial):
```

## Advanced Features

### Add Obstacle Avoidance
```python
# Emergency stop for close obstacles
if min(left_dist, right_dist) < 5:
    bot.stop()
    time.sleep(0.5)
    bot.backward(70)
    time.sleep(1)
```

### Implement PID Control
```python
# Simple proportional control upgrade
error = left_dist - right_dist
integral += error * dt
derivative = (error - last_error) / dt

# PID formula
steering = Kp * error + Ki * integral + Kd * derivative
angle = CENTER + constrain(steering, -MAX_ANGLE, MAX_ANGLE)
```

### Add Path Memory
```python
path_history = []
position_estimate = {"x": 0, "y": 0, "heading": 0}

# Log movements
path_history.append({
    "time": time.time(),
    "left": left_dist,
    "right": right_dist,
    "steering": angle
})
```

## Troubleshooting

### Serial Communication Issues:
- **"No data received"**: Check Arduino is sending data
- **"Malformed line"**: Verify Arduino data format
- **Permission denied**: Add user to dialout group
  ```bash
  sudo usermod -a -G dialout $USER
  ```

### Camera Issues:
- **Black screen**: Enable camera in `raspi-config`
- **Import error**: Install picamera2 dependencies
- **Slow performance**: Reduce resolution

### Navigation Problems:
- **Hitting walls**: Increase MAX_ANGLE or sensitivity
- **Zigzag movement**: Decrease sensitivity or add smoothing
- **Not turning**: Check servo connections and limits

## Performance Optimization

### 1. Reduce Serial Latency
```python
# Add to setup
ser.set_low_latency_mode(True)
```

### 2. Optimize Image Processing
```python
# Skip frames for display
frame_count = 0
if frame_count % 5 == 0:  # Show every 5th frame
    cv2.imshow("Camera", img_bgr)
frame_count += 1
```

### 3. Multi-threading
```python
import threading

def camera_thread():
    while running:
        img = picam2.capture_array()
        # Process image
        
def sensor_thread():
    while running:
        data = leer_datos3()
        # Process sensors
```
## Schemes

## v-photos



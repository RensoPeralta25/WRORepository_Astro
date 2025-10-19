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

* **`schemes`** - Contains electromechanical schematic diagrams (JPEG/PNG/PDF format) illustrating:
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

## ⚙️ Models

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


### 🚀 First Prototype Design

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/3b4e8dc8-8090-4ecc-8f10-5860a87f4374" />

Our first prototype was designed with a minimalist yet strategic approach to sensor integration and mechanical structure. The initial concept called for five ultrasonic sensors strategically distributed around the chassis to provide full 360-degree obstacle detection coverage: a front-facing center sensor for primary detection, two front-facing sensors angled at 45° (left and right) to cover side blind spots, and two side sensors at 90° for wall following and narrow-space detection.

### 🚀 Second Prototype Design

After having thought about this sketch, for reasons of optimizing the position of sensors, we decided to completely change the design of our autonomous robot. As mentioned before, we wanted to have 6 ultrasonics, to help us have more vision.

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/1e7915e2-b183-4115-982e-7833c104bb1c" />

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/5bd1bc20-b3f7-4b07-879e-12e24e8cacb6" />

## 🔧 Challenges and Solutions During Final Design

During the development and assembly of our autonomous vehicle, we encountered several technical challenges that required creative solutions and design modifications. These challenges taught us valuable lessons about iterative design and practical engineering problem-solving.

One of the first challenges we faced was fitting the color sensor into its designated mounting space. The original CAD design did not account for the actual physical dimensions and connector orientation of the TCS 3200 color sensor module.

**Problem:** The color sensor module, including its I2C connector pins, exceeded the allocated space in the front sensor mount structure. The rigid PCB design prevented us from repositioning it without structural modifications.

**Solution:** We used a soldering iron to carefully create a custom opening in the plastic chassis mount. This allowed us to recess the sensor body while keeping the optical window at the optimal height and angle for line detection. The modification maintained the sensor's downward-facing orientation (approximately 30-45° angle) necessary for accurate color detection of the track surface while minimizing ambient light interference.

**Result:** The color sensor was successfully integrated and provided reliable line detection throughout testing.

#### Ultrasonic Sensor Reduction

Our initial design included six HCSR04 ultrasonic sensors for comprehensive 360° obstacle detection coverage. However, physical constraints and spatial optimization led to significant changes.

**Problem:** The front-mounted color sensor required substantial space in the frontal area of the chassis. Installing the two front-angled ultrasonic sensors (positioned at 45° left and right) would have created physical interference with both the color sensor mount and its cable routing. Additionally, the overall chassis space was more limited than anticipated in the CAD model.

**Solution:** We strategically removed four of the six ultrasonic sensors:
- **Two front sensors (45° angled):** Removed due to space conflict with the color sensor assembly
- **Two additional sensors:** Removed to optimize weight distribution and simplify wiring complexity

We retained only the two most critical ultrasonic sensors:
- **Front-center sensor:** For primary forward obstacle detection
- **One side sensor:** For wall-following and lateral distance measurement

**Trade-off Analysis:** While this reduced our sensor coverage from 360° to bilateral coverage, our testing revealed that the remaining sensors, combined with the camera's computer vision capabilities and IMU data, still provided sufficient environmental awareness for successful navigation.

#### Rear Wheel Support Structure Failure

**Problem:** The 3D-printed rear wheel support arms, designed to hold rubber tires in place, experienced structural failure during initial testing. The stress concentration points where the tires connected to the motor shafts caused the plastic supports to crack and eventually break. This was likely due to:

- Insufficient wall thickness in the 3D-printed part
- Vibrations from the DC motors during operation
- Lateral forces during turning maneuvers

**Solution:** Unable to quickly redesign and reprint the support structure, we implemented an emergency repair using a soldering iron technique:
1. We carefully heated the soldering iron to a temperature suitable for melting PLA/ABS plastic
2. We repositioned the broken rubber tire holders against the motor mounting arms
3. We used the soldering iron tip to "weld" the plastic pieces together, creating a reinforced joint
4. We added additional plastic material where needed to strengthen critical stress points

**Result:** This field repair successfully restored structural integrity and proved durable enough for the remainder of our testing and competition preparation. However, this experience highlighted the importance of stress testing 3D-printed components and designing with appropriate safety margins for dynamic loads.

Our electronic architecture underwent a significant simplification during the final assembly phase.

**Original Plan:** Arduino Mega 2560
- **Reason for selection:** The Mega provides 54 digital I/O pins and 16 analog inputs, which we initially believed necessary to accommodate six ultrasonic sensors (12 digital pins), the color sensor (I2C), the IMU (I2C), servo motors (2 PWM pins), and the DC motor driver (4 digital pins).

**Modified Implementation:** Arduino Uno R3
- **Reason for change:** After reducing the ultrasonic sensor count from six to two, the total pin requirement decreased significantly:
  - 2 ultrasonic sensors: 4 digital pins (2 trigger + 2 echo)
  - Color sensor: I2C bus (SDA/SCL) - 2 pins
  - IMU (BNO055): I2C bus (shared) - 0 additional pins
  - Servo motor (steering): 1 PWM pin
  - DC motor driver: 2-4 digital pins
  - **Total: approximately 9-11 pins**

The Arduino Uno R3 provides 14 digital I/O pins and 6 analog inputs, which is more than sufficient for our reduced configuration. This change offered several advantages:
- **Reduced physical footprint:** The Uno is smaller and lighter than the Mega
- **Improved space utilization:** Easier to fit within the chassis alongside other components
- **Cost optimization:** Lower component cost without sacrificing functionality
- **Simplified wiring:** Fewer unused pins reduced wiring complexity

### Power Distribution Solution

Managing multiple 5V power connections for sensors and modules with limited power pins on the Arduino.

**Solution:** We implemented a breadboard-based power distribution system:
- **Positive rail (5V):** Connected to Arduino's 5V output pin
- **Ground rail (0V/GND):** Connected to Arduino's GND pin
- **Connected devices:** All sensors requiring 5V power (ultrasonic sensors, color sensor) were connected to the breadboard rails

**Advantages:**
- Organized and accessible power distribution
- Easy troubleshooting and component replacement
- Reduced stress on Arduino's voltage regulator by distributing current load
- Clean cable management

**Considerations:** We ensured that the total current draw from all 5V devices did not exceed the Arduino's maximum output current (approximately 500mA from USB or 800-1000mA from VIN regulator).

## 💻 Sources (src)







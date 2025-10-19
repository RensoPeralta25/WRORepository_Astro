# WRO Repository TEAM Astro

## Team Information

Team name: Astro

📜 Renso Isael Peralta Ureña (Right)

🧑‍🔧 José Miguel Comprés Arias (Left)

🧑‍🔧 Yoel Samuel Castillo Castillo (Front)

![team photo](https://github.com/user-attachments/assets/d0d88cb5-2361-492b-bfa1-58ac8055714e)

PUCMM, Dominican Republic <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/cacb6bc7-76ba-49e5-9df6-87c6d36aa328" />

## Content Organization

This repository contains the complete documentation and resources for our autonomous vehicle designed for the WRO 2025 Future Engineers category.

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
  * Challenge #1
  * Challenge #2

* **`schemes`** - Contains electromechanical schematic diagrams (JPEG/PNG/PDF format) illustrating:
  * Electronic components layout (Raspberry Pi 5, Arduino Mega, Robot Hat v4)
  * Sensor connections (4 ultrasonic sensors, color sensor, IMU, camera)
  * Motor connections and power distribution
  * Complete wiring diagram showing all component interconnections

* **`src`** - Contains the control software source code:
  * Python scripts for Raspberry Pi 5 (high-level processing, computer vision)
  * Arduino code for real-time sensor and motor control
  * Communication protocols between Raspberry Pi and Arduino
  * Sensor processing modules (ultrasonic, color sensor, IMU)
  * Navigation and decision-making algorithms

* **`models`** - Contains 3D models and design files:
  * CAD files for chassis components
  * STL files for 3D-printed parts (sensor mounts, camera holder, structural elements)
  * First prototype design files
  * Second prototype design files (optimized version)

## Introduction
This project presents our autonomous vehicle designed for the 2025 World Robot Olympiad (WRO) competition in the Future Engineers category. The robot is fully autonomous, capable of navigating a closed course, detecting and avoiding objects, and parking itself at the end of the course.

### What Makes Our Design Unique

Our vehicle stands out for its redundant and robust sensor architecture: it integrates four strategically positioned ultrasonic sensors that provide full 360° perimeter detection, a color sensor for precise object identification, and an IMU (Inertial Measurement Unit) that allows the robot to maintain orientation and stability in real time.

The brain of the system is a state-of-the-art Raspberry Pi 5 working in conjunction with an Arduino Mega via the Robot Hat v4, creating a dual architecture that separates high-level processing (vision and decision-making) from real-time control (motors and sensors). This hybrid configuration guarantees ultra-fast responses and system stability.

Visually, the robot features a futuristic, technological design in white, reflecting innovation and modernity. The precision servo steering system ensures smooth and accurate maneuvers, while data fusion from multiple sensors enables reliable autonomous navigation even in challenging track conditions.

## ⚙️ Models

### Components
- **Main Controller**: Raspberry Pi 5 (high-level processing)
- **Real-time Controller**: Arduino UNO R3
- **Interface Board**: Robot Hat v4
- **Sensors**:
  - 2x Ultrasonic sensors HCSR04 (Bilateral coverage)
  - 1x Color sensor TCS 3200 (line detection)
  - 1x IMU MPU-9250 (orientation)
  - 1x Raspberry Pi Camera (computer vision)
- **Motors**: TT Motor x1
- **Power Source**: Battery

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







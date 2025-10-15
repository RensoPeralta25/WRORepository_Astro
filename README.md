# WRO Repository TEAM Astro

## Team Information

Team name: Astro

Renso Isael Peralta Ureña
José Miguel Comprés Arias
Yoel Samuel Castillo Castillo

PUCMM, Dominican Republic

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
  * Line Following demonstration
  * Traffic Sign Detection
  * Obstacle Avoidance
  * Autonomous Parking
  * Full course run (minimum 30 seconds each)

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
  * Assembly drawings and specifications

* **`other`** - Contains additional documentation:
  * Hardware setup instructions for Raspberry Pi 5
  * Dependency installation guide (requirements.txt)
  * Communication protocol documentation between boards
  * Sensor calibration procedures
  * Deployment and testing guidelines

## Introduction
This project presents our autonomous vehicle designed for the 2025 World Robot Olympiad (WRO) competition in the Future Engineers category. The robot is fully autonomous, capable of navigating a closed course, detecting and avoiding objects, and parking itself at the end of the course.

### What Makes Our Design Unique

Our vehicle stands out for its redundant and robust sensor architecture: it integrates four strategically positioned ultrasonic sensors that provide full 360° perimeter detection, a color sensor for precise object identification, and an IMU (Inertial Measurement Unit) that allows the robot to maintain orientation and stability in real time.

The brain of the system is a state-of-the-art Raspberry Pi 5 working in conjunction with an Arduino Mega via the Robot Hat v4, creating a dual architecture that separates high-level processing (vision and decision-making) from real-time control (motors and sensors). This hybrid configuration guarantees ultra-fast responses and system stability.

Visually, the robot features a futuristic, technological design in white, reflecting innovation and modernity. The precision servo steering system ensures smooth and accurate maneuvers, while data fusion from multiple sensors enables reliable autonomous navigation even in challenging track conditions.

## ⚙️ Vehicle Design

### Drive System
*[Add information about differential rear-wheel or other drive system]*

### Components
- **Main Controller**: Raspberry Pi 5 (high-level processing)
- **Real-time Controller**: Arduino Mega (motor and sensor control)
- **Interface Board**: Robot Hat v4
- **Sensors**:
  - 4x Ultrasonic sensors (360° coverage)
  - 1x Color sensor (line detection)
  - 1x IMU (orientation and stability)
  - 1x Camera (computer vision)
- **Motors**: *[Specify type and quantity]*
- **Power Source**: *[Specify battery type and specifications]*

### 🚀 First Prototype Design

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/3b4e8dc8-8090-4ecc-8f10-5860a87f4374" />

Our first prototype was designed with a minimalist yet strategic approach to sensor integration and mechanical structure. The initial concept called for five ultrasonic sensors strategically distributed around the chassis to provide full 360-degree obstacle detection coverage: a front-facing center sensor for primary detection, two front-facing sensors angled at 45° (left and right) to cover side blind spots, and two side sensors at 90° for wall following and narrow-space detection.

*[Continue with existing first prototype description...]*

### 🚀 Second Prototype Design

After having thought about this sketch, for reasons of optimizing the position of sensors, we decided to completely change the design of our autonomous robot. As mentioned before, we wanted to have 6 ultrasonics, to help us have more vision.

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/1e7915e2-b183-4115-982e-7833c104bb1c" />

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/5bd1bc20-b3f7-4b07-879e-12e24e8cacb6" />


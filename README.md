# WRO Repository TEAM Astro
## Introduction
This project presents our autonomous vehicle designed for the 2025 World Robot Olympiad (WRO) competition in the Future Engineers category. The robot is fully autonomous, capable of navigating a closed course, detecting and avoiding objects, and parking itself at the end of the course. 

What makes our design unique:

Our vehicle stands out for its redundant and robust sensor architecture: it integrates four strategically positioned ultrasonic sensors that provide full 360° perimeter detection, a color sensor for precise object identification, and an IMU (Inertial Measurement Unit) that allows the robot to maintain orientation and stability in real time.

The brain of the system is a state-of-the-art Raspberry Pi 5 working in conjunction with an Arduino Mega via the Robot Hat v4, creating a dual architecture that separates high-level processing (vision and decision-making) from real-time control (motors and sensors). This hybrid configuration guarantees ultra-fast responses and system stability.

Visually, the robot features a futuristic, technological design in white, reflecting innovation and modernity. The precision servo steering system ensures smooth and accurate maneuvers, while data fusion from multiple sensors enables reliable autonomous navigation even in challenging track conditions.
## ⚙️ Vehicle Design
- Drive system (e.g., differential rear-wheel)
- Motors (type and quantity) and power source (battery type and specs)
- Sensors used (line, distance, vision) and their location
- Brief summary of CAD and physical layout

### 🚀 First Prototype Design

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/3b4e8dc8-8090-4ecc-8f10-5860a87f4374" />

Our first prototype was designed with a minimalist yet strategic approach to sensor integration and mechanical structure. The initial concept called for five ultrasonic sensors strategically distributed around the chassis to provide full 360-degree obstacle detection coverage: a front-facing center sensor for primary detection, two front-facing sensors angled at 45° (left and right) to cover side blind spots, and two side sensors at 90° for wall following and narrow-space detection. Additionally, a color sensor was integrated into a protruding rectangular structure on the front of the robot, specifically designed to position the sensor at an optimal height with a downward tilt angle to allow for accurate detection of the black circuit line, while minimizing ambient light interference thanks to its wraparound design. For advanced navigation and obstacle recognition, a camera was mounted on the top center of the chassis, enabling visual processing to identify and classify obstacles using computer vision algorithms. Finally, an IMU (Inertial Measurement Unit) was positioned on top of the robot, directly above the center of gravity, to provide precise orientation data (yaw, pitch, and roll angles) and stabilization during navigation, crucial for maintaining straight trajectories and executing turns with angular precision. The mechanical structure was complemented by front arms specifically designed for mounting the front wheels, providing an independent steering system that improves maneuverability and allows for precise turning radius adjustments. The rectangular configuration of the front color sensor mount not only fulfills its sensory function but also acts as a structural element that reinforces the front of the chassis and provides protection against minor impacts.

### 🚀 Second Prototype Design

After having thought about this sketch, for reasons of optimizing the position of sensors, we decided to completely change the design of our autonomous robot. As mentioned before, we wanted to have 6 ultrasonics, to help us have more vision. We took this into account for the next version of the design, and also at first we did not think about the location of the engine, this was optimized.

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/1e7915e2-b183-4115-982e-7833c104bb1c" />

<img width="611" height="300" alt="image" src="https://github.com/user-attachments/assets/5bd1bc20-b3f7-4b07-879e-12e24e8cacb6" />

## 🧠 Software Architecture
- Overview of your control strategy
- Code modules (e.g., `line_tracking.py`, `sign_detection.py`)
- Communication or data flow between modules
- Programming language(s) and runtime platform (e.g., Raspberry Pi, Arduino)
## 🔧 Build Instructions
- List of all components used (with part numbers or links if possible)
- Step-by-step physical assembly instructions
- CAD file references or screenshots
## 💾 Code Deployment
- How to set up the environment
- How to install dependencies (requirements.txt)
- How to upload/execute code on your platform
- Any hardware-specific notes or configurations
## 🎥 Test and Evaluation Videos
- Add public links to at least 30-second videos for each required task:
  - Line Following
  - Traffic Sign Detection
  - Obstacle Avoidance
  - Autonomous Parking
- Include a brief description of each video

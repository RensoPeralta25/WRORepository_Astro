#🚀 First Prototype Design
#Initial Sketch and Concept
--------------------------------
Our first prototype was designed with a minimalist yet strategic approach to sensor integration and mechanical structure. 
The initial concept called for five ultrasonic sensors strategically distributed around the chassis to provide full 
360-degree obstacle detection coverage: a front-facing central sensor for primary detection, two front-facing sensors 
angled at 45° (left and right) to cover lateral blind spots, and two side sensors at 90° for wall following and narrow-space 
detection. Additionally, a color sensor was integrated into a rectangular protruding structure on the front of the robot, 
specifically designed to position the sensor at an optimal height (5-10 mm from the ground) with a downward tilt angle to 
allow for accurate detection of the black circuit line, while minimizing ambient light interference thanks to its wraparound 
design. For advanced navigation and obstacle recognition, a camera (OpenMV Cam H7 or Raspberry Pi Camera Module) was mounted 
on the top center of the chassis at a height of approximately 15-20cm, with a slight forward tilt to capture the approaching 
section of the circuit, thus enabling visual processing to identify and classify obstacles using computer vision algorithms. 
Finally, an IMU (Inertial Measurement Unit) was positioned on top of the robot, directly above the center of gravity, to provide 
accurate orientation data (yaw, pitch, and roll angles) and stabilization during navigation, crucial for maintaining straight 
trajectories and executing turns with angular precision. The mechanical structure was complemented by front arms specifically 
designed for mounting the front wheels, providing an independent steering system that improves maneuverability and allows precise 
turning radius adjustments. The rectangular configuration of the front color sensor mount not only fulfills its sensory function 
but also acts as a structural element that reinforces the front of the chassis and provides protection against minor impacts.


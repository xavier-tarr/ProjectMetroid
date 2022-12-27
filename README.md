# ProjectMetroid
Project Metroid

The goal of this project was to design and build a dual hexapod robot from scratch. The robot would have six legs on the top and six legs on the bottom, each connected to spherical shells that had friction-filled bottoms to enable walking. This project was completed in the fall of 2017.

The robot was also designed to be able to scrunch itself inward to form a ball, which it would then use specific gaits to roll around. The robot was controlled using a Raspberry Pi 2 and could be remotely controlled. 

It includes a 9 degree of freedom IMU (inertial measurement unit) to provide orientation data for the robot's decision making. The robot was built using 3D printed parts and servo motors. In the end, the 3D printed legs were not strong enough to support the full weight of the 36 servo motors and their connectors. Although this projects has successful walking gaits for half of the robot.

The robot was intended to be able to operate remotely using a hotspot and wireless chip added to the Raspberry Pi, as well as two battery packs to power the Raspberry Pi and motors. The project included the creation of custom classes and functions to control the servo motors and IMU sensor, as well as various gait functions to allow the robot to walk and roll.
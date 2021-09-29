# ROS Ultimate Guide for Beginners with TurtleBot3 and Robot
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Link-to-the-Course">Link to the Course</a></li>
    <li><a href="#Notes">Features</a></li>
    <li><a href="#Instructors">Instructors</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
ROS1 Noetic is the main framework we will be using in this course , Turtlesim package , TurtleBot3 and our Custom Robot Dolly is what we are going to create add sensors to these robots and write algorithms to avoid obstacles in simulation of Gaebo

- ![alt text](https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot/blob/main/Images/mainCover.png)
- **[[Get course Here]](https://www.udemy.com/course/the-ultimate-guide-to-ros-simulate-your-robots/?couponCode=GITHUB)**
----
## Using this Repository
* Move into your workspace/src folder
 ```
 cd path/to/ros1_ws/src/
##e.g cd ~/catkin_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot
```


* Perform make and build through catkin
 ```
 cd /path/to/workspace_root/
 ##e.g ~/catkin_ws/
 catkin_make
 ```
 
* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/catkin-ws/devel/setup.bash
```
- (Optional for Power USERs only) Add source to this workspace into bash file
 ```
echo "source /path/to/catkin-ws/devel/setup.bash" >> ~/.bashrc
 ```
  **NOTE:** This upper command is going to add the source file path into your ~/.bashrc file ( Only perform it once and you know what you are doing).This will save your time when running things from the Workspace

----
## Course Workflow
- We will get some basics of ROS1 with the help of in-built ROS1 package **TurtleSim** . Then we will move toward very useful concepts which are nodes , package, topic -> Publishing/Subscribing

- We will deep dive into a **TurtleBot3** robot package and understand how it is built and how we can manipulate it .

- This will lead us towards creation of our new package **Dolly** which is a car that we will be creating from scratch using URDF xml syntax . Next we will create its Gazebo and RVIZ1 3D simulator . Then we will add Differential Drive Plugin in our robot and drive it .

With these simulators endless possibilities of projects will open by adding the virtual sensors to your Robot.


---
## Features
* **TurtleSim Circle Movement** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot/blob/main/Images/turtleSim_circle.gif)
* **Turtlebot 3 Object Irrirational Robot** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot/blob/main/Images/tb3_irritated.gif)
* **Building Custom Robot** 
  -  ![alt text](https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot/blob/main/Images/building_dolly.gif)
* **Obstacle Avoiding Robot**
  - ![alt text](https://github.com/noshluk2/ROS-Ultimate-Guide-for-Beginners-with-TurtleBot3-and-Robot/blob/main/Images/dolly_OA.gif)
* 


----
## Pre-Course Requirments 

**Software Based**
* Ubuntu 20.04 (LTS)
* ROS1 - Noetic
---
## Link to the Course
<!-- - ![alt text](https://github.com/HaiderAbasi/SelfDrivingProject_MiniTesla/blob/master/3D%20model%20file/Tesla%20Self%20Driving%20Car.png) -->

**[[Get course HERE]](https://www.udemy.com/course/the-ultimate-guide-to-ros-simulate-your-robots/?couponCode=GITHUB)**

----

## Instructors

Muhammad Luqman (ROS Simulation and Control Systems) - [Profile Link](https://www.linkedin.com/in/muhammad-luqman-9b227a11b/)  

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.

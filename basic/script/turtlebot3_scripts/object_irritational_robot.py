#!/usr/bin/env python
import rospy
import numpy as np
from numpy import inf

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class object_irritation_robot:

    def __init__(self):
        rospy.Subscriber("/scan" , LaserScan, self.laser_scanner_callback)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.robot_velocity=Twist()

    def laser_scanner_callback(self,data):
        laser_data=np.array(data.ranges)
        
        laser_data[laser_data == inf] = 0

        max_value=max(laser_data)
        rospy.loginfo("Maximum value from the laser scanner = %f",max_value)

        if(max_value > 0.6):
            self.irritated()
        else: 
            self.move_forward()

        self.pub.publish(self.robot_velocity)

    def move_forward(self):
        rospy.loginfo("Going Forward")
        self.robot_velocity.linear.x=.20
        self.robot_velocity.angular.z= 0.0
    def irritated(self):
        rospy.loginfo("I am Irritated")
        self.robot_velocity.linear.x=0.0
        self.robot_velocity.angular.z= 1.57


 
if __name__ == '__main__':
    rospy.init_node('object_irritation_robot', anonymous=True)
    object_irritation_robot()
    rospy.spin()
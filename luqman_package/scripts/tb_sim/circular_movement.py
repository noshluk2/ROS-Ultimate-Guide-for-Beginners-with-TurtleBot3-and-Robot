#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def circular_movement_node():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('tbsim_driver', anonymous=True)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        robot_velocity =Twist()
        robot_velocity.linear.x =2.0
        robot_velocity.angular.z=0.5
        pub.publish(robot_velocity)
        rate.sleep()

if __name__ == '__main__':
    try:
        circular_movement_node()
    except rospy.ROSInterruptException:
        pass
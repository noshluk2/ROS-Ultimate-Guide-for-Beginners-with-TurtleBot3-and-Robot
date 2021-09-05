#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist



def irritated():
    rospy.loginfo("I am Irritated")
    robot_velocity=Twist()
    robot_velocity.angular.z= 1.57
    r = rospy.Rate(5.0)
    while(1):
        pub.publish(robot_velocity)
        r.sleep()


def main():
    global pub
    rospy.init_node('Custom_driver', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        robot_velocity=Twist()
        robot_velocity.linear.x= 1.0
        robot_velocity.angular.z= 1.57
        pub.publish(robot_velocity)
        rate.sleep()




if __name__ == '__main__':
    main()
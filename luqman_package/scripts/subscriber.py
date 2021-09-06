#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def this_course(data):
    rospy.loginfo("I took %s", data.data)
    
def listener():

    rospy.init_node('You', anonymous=True)
    rospy.Subscriber("Udemy", String, this_course)
    rospy.spin()

if __name__ == '__main__':
    listener()
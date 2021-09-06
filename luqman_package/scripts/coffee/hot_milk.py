#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('ingredients', String, queue_size=10)
    rospy.init_node('hot_milk', anonymous=True)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        string_ = "Hot Milk"
        pub.publish(string_)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
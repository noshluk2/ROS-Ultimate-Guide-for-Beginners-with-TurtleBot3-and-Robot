#!/usr/bin/python3


import rospy
from std_msgs.msg import String

def sugar_publisher():
    pub = rospy.Publisher('ingredients', String, queue_size=10)
    rospy.init_node('sugar', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        sugar_chunks = "White Sugar"
        rospy.loginfo(sugar_chunks)
        pub.publish(sugar_chunks)  
        rate.sleep()

if __name__ == '__main__':
    try:
        sugar_publisher()
    except rospy.ROSInterruptException:
        pass
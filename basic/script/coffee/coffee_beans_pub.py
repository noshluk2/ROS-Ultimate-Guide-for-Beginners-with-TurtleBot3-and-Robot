#!/usr/bin/python3


import rospy
from std_msgs.msg import String

def coffee_beans_publisher():
    pub = rospy.Publisher('ingredients', String, queue_size=10)
    rospy.init_node('coffee_beans', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        sugar_chunks = "Crushed Coffee Beans"
        rospy.loginfo(sugar_chunks)
        pub.publish(sugar_chunks)  
        rate.sleep()

if __name__ == '__main__':
    try:
        coffee_beans_publisher()
    except rospy.ROSInterruptException:
        pass
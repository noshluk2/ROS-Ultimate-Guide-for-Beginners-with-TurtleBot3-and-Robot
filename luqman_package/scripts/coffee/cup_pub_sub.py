#!/usr/bin/python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

def mixer_callback(data):
    global counter , cup
    counter = counter + 1
    if(counter==3):
        cup=cup +1 
        rospy.loginfo("Cup # %s is ready ",cup)
        pub.publish(cup)
        counter=0;
    
def listener():
    global pub
    rospy.init_node('Cup', anonymous=True)
    rospy.Subscriber("ingredients", String, mixer_callback)
    pub = rospy.Publisher('ready_cups', Int16, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    counter=0
    cup=0
    listener()
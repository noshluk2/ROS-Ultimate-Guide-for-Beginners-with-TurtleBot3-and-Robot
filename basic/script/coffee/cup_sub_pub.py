#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback_ingredients(data):

    rospy.loginfo("I added %s", data.data)
    rospy.loginfo(" Coffee is ready to drink ")
    pub.publish(data)

def coffee_ready_cup():
    global pub
    rospy.init_node('coffee_cup'    , anonymous=True)
    rospy.Subscriber("ingredients" , String, callback_ingredients)
    pub = rospy.Publisher('cup_ready', String, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    coffee_ready_cup()
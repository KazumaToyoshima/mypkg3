#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

import rospy
from std_msgs.msg import Int32

n = 0
m = 0

def cb(message):
        global n
        n = message.data%12

def cd2(message):
        global m
        m = message.data


if __name__=='__main__':
        rospy.init_node('time')
        pub = rospy.Publisher('timer1', Int32, queue_size = 1)
        pub2 = rospy.Publisher('timer2', Int32, queue_size = 1)
        sub = rospy.Subscriber('second_up',Int32,cb)
        sub2 = rospy.Subscriber('min',Int32,cd2)
        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
                pub.publish(n)
                pub2.publish(m)
                rate.sleep()

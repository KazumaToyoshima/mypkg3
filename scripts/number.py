#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.
#*Copyright(c)2021 Kazuma Toyoshima. All rights reserved.

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
        global n
        n = message.data%12


if __name__=='__main__':
        rospy.init_node('number')
        pub = rospy.Publisher('number', Int32, queue_size = 1)
        sub = rospy.Subscriber('count_up',Int32,cb)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
                pub.publish(n)
                pub2.publish(m)
                rate.sleep()

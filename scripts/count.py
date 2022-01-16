#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.
#*Copyright(c)2021 Kazuma Toyoshima. All rights reserved.

import rospy
from std_msgs.msg import Int32


rospy.init_node('count')
pub = rospy.Publiser('count_up', Init32, queue_size=1)
rate = rospy.Rate(10)
n = 10
while not rospy.is_shutdown():
    n += 2
    pub.publish(n)
    rate.sleep()

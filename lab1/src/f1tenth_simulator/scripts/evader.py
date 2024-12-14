#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
from numpy import mean


def callback(msg):
    ranges = msg.ranges

    dis_avg = mean(ranges[500:580])
    if dis_avg < 3:
        publisher(2.0,0.5)
    else:
        publisher(2.0,0.0)


def publisher(speed,turn):

    ack_pub = rospy.Publisher('/evader_drive', AckermannDriveStamped, queue_size=10)
    ack_msg_st = AckermannDriveStamped()
    ack_msg_st.header.stamp = rospy.Time.now()
    ack_msg_st.drive.steering_angle = turn
    ack_msg_st.drive.speed = speed
    ack_pub.publish(ack_msg_st)


rospy.init_node('evader')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()

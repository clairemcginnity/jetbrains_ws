#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32

from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Point32


class Observer:

	def __init__(self):

		self.observer_sub = rospy.Subscriber('position', Float32MultiArray, self.callback)
		self.path_msg = PointCloud()

		self.path_pub = rospy.Publisher('path_topic', PointCloud, queue_size=10)
		self.path_msg.header.frame_id = "base_link"

	def callback(self, coords):
		x = coords.data[0]
		y = coords.data[1]

		self.path_msg.points.append(Point32(x,y,0))
		self.path_pub.publish(self.path_msg)

if __name__ == '__main__':
	rospy.init_node('observer')
	observer = Observer()
	rospy.spin()
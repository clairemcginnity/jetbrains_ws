#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32

from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Point32


class Observer:

	def __init__(self):
		#subcsribe to the position topic that runner publishes to
		self.observer_sub = rospy.Subscriber('position', Float32MultiArray, self.callback)
		#use point cloud msg type to visually represent the path of the runner
		self.path_msg = PointCloud()
		self.path_pub = rospy.Publisher('path_topic', PointCloud, queue_size=10)
		self.path_msg.header.frame_id = "base_link"

	def callback(self, coords):
		#Create Point32 object from coordinates and add to PointCloud message
		#PointCloud message stores all coordinates so far and displays them 
		x = coords.data[0]
		y = coords.data[1]
		#publish visual representation of runner's path
		self.path_msg.points.append(Point32(x,y,0))
		self.path_pub.publish(self.path_msg)

if __name__ == '__main__':
	rospy.init_node('observer')
	observer = Observer()
	rospy.spin()

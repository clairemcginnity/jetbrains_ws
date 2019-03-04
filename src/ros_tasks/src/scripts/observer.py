#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32

def callback(coords):
	x = coords.data[0]
	y = coords.data[1]
	z = coords.data[2]

	print('x: ' + str(x) + ', y: ' + str(y) + ' z: ' + str(z))
	#pub.publish(1.0)

def observer():
	rospy.Subscriber('position', Float32MultiArray, callback)
	rospy.spin()

if __name__ == '__main__':
	rospy.init_node('observer')
	#pub = rospy.Publisher('check', Float32, queue_size=10)
	observer()
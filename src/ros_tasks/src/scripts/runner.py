#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
import math

class Runner:

  #move in cyclindrical co-ordinates with R = 1, z = 1 and theta varying

  def __init__(self):
    #set up publisher node and rate
    self.theta = 0
    self.runner_pub = rospy.Publisher('position', Float32MultiArray, queue_size=10)
    self.r = rospy.Rate(1)
    try:
        self.runner()
    except rospy.ROSInterruptException:
        pass
    
  def runner(self):

    while not rospy.is_shutdown():
      #move in a circle in increments of pi/16
      x = math.cos(self.theta)
      y = math.sin(self.theta)
      self.theta += math.pi/16
      
      #use std message type Float32MultiArray to store coordinates
      msg = Float32MultiArray()
      msg.layout.dim.append(MultiArrayDimension())
      msg.layout.dim[0].label = "coords"
      msg.layout.dim[0].size = 3
      msg.layout.data_offset  = 0
      msg.data = [0]*3
       
      msg.data[0] = x
      msg.data[1] = y
      msg.data[2] = 1.0
      
      #publish msg
      self.runner_pub.publish(msg)
      
      self.r.sleep()

if __name__ == '__main__':
  rospy.init_node('runner')
  runner = Runner()
  rospy.spin()

#include <iostream>
#include "ros/ros.h"
#include "std_msgs/Float32MultiArray.h"
#include <string>

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
using namespace std;
void observerCallback(const std_msgs::Float32MultiArray::ConstPtr& msg)
{
//  msg->data;
	std::cout<< "[" << msg->data[0] << ", " << msg->data[1] <<  ", "  << msg->data[2] << "]" << std::endl;

}

int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "observer");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("position", 1000, observerCallback);
  ros::spin();

  return 0;
}
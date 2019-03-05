#include <iostream>
#include "ros/ros.h"
#include "std_msgs/Float32MultiArray.h"
#include <string>

using namespace std;
void observerCallback(const std_msgs::Float32MultiArray::ConstPtr& msg)
{
//  print coordinates to console in the form [x, y, z]
	std::cout<< "[" << msg->data[0] << ", " << msg->data[1] <<  ", "  << msg->data[2] << "]" << std::endl;

}

int main(int argc, char **argv)
{
  //initialize subscriber node and subcribe to position topic to which runner publishes
  ros::init(argc, argv, "observer");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("position", 1000, observerCallback);
  ros::spin();

  return 0;
}

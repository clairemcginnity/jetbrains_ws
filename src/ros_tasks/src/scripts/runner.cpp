#define _USE_MATH_DEFINES
#include "ros/ros.h"
#include "std_msgs/Float32MultiArray.h"
#include "cmath"
#include <iostream>
#include <sstream>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "runner");
	ros::NodeHandle n;
	ros::Publisher runner_pub = n.advertise<std_msgs::Float32MultiArray>("position", 10);
	ros::Rate loop_rate(1);

	float theta = 0;
	float x = 0;
	float y = 0;
	float z = 0;


	int count = 0;
	while (ros::ok())
	{
		std_msgs::Float32MultiArray msg;

		msg.layout.dim.push_back(std_msgs::MultiArrayDimension());
		msg.layout.dim[0].size = 3;	
		msg.layout.dim[0].label = "coord";
		msg.layout.data_offset = 0;
		msg.data.clear();  

		theta = count*M_PI*0.125;

		x = cos(theta);
		y = sin(theta);
		z = tan(theta);

		msg.data.push_back(x);
		msg.data.push_back(y);
		msg.data.push_back(z);

		runner_pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
		++count;
	}
	return 0;
}

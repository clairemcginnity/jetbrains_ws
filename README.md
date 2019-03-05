# jetbrains_ws

##### once you have cloned the reposistory from ~/jetbrains_ws run 

```
$ catkin_make
```
```
$ source devel/setup.bash
```

##### Start roscore in the background

##### then you can run the tasks using the following
```
$ roslaunch ./src/ros_tasks/src/launch/launch_task1_cpp.launch
```
```
$ roslaunch ./src/ros_tasks/src/launch/launch_task2_python.launch
```

##### For task1 the coordinates of the runner should begin to print to the console from which you launch the file
##### For task2 you should open a new terminal and run rviz
##### Under Global Options set Fixed Frame to base_link
##### Click Add and under By topic select /path_topic PointCloud
##### Under PointCloud set size = 0.1m
##### The path should be visible in the rviz window

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

  # Start robot localization using an Extended Kalman filter
  start_obstacles_detection = Node(
    package='rtabmap_util',
    executable='obstacles_detection',
    name='obstacles_detection',
    output='screen',
    parameters=[{"frame_id": "camera_link"},
                {"queue_size": 10},
                {"max_obstacles_height": 0.0},],
    remappings=[('cloud', '/camera/depth/color/points'),
                ('ground', '/rtabmap/ground'),
                ('obstacles', '/rtabmap/obstacles')] 
    )

  # Create the launch description and populate
  ld = LaunchDescription()
  ld.add_action(start_obstacles_detection)

  return ld
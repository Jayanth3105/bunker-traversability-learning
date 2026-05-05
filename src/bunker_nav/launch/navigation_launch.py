from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os

def generate_launch_description():
    
     
    pkg_share = FindPackageShare(package='bunker_nav').find('bunker_nav')

    nav_file_path = os.path.join(pkg_share, 'config/nav2_params.yaml') 
    # nav_file_path = os.path.join(pkg_share, 'config/human_following.yaml') #try purepursuit

    bunker_base_launch_path = PathJoinSubstitution(
        [FindPackageShare("nav2_bringup"),
        "launch",
        "navigation_launch.py"],
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([bunker_base_launch_path]),
        launch_arguments={
                'params_file': nav_file_path,
                # 'params_file': 'false',
                }.items(),
    )


    ld = LaunchDescription()
    ld.add_action(navigation_launch)


    return ld

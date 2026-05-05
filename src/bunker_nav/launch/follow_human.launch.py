from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()
     
    # pkg_share = FindPackageShare(package='bunker_nav').find('bunker_nav')

    # nav_file_path = os.path.join(pkg_share, 'config/human_following.yaml') 

    # bunker_base_launch_path = PathJoinSubstitution(
    #     [FindPackageShare("nav2_bringup"),
    #     "launch",
    #     "navigation_launch.py"],
    # )

    # navigation_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([bunker_base_launch_path]),
    #     launch_arguments={
    #             'params_file': nav_file_path,
    #             # 'params_file': 'false',
    #             }.items(),
    # )

    config = os.path.join(
        get_package_share_directory('bunker_nav'),
        'config',
        'human_following.yaml'
        )
        
    human_detection=Node(
        package = 'bunker_vis',
        name = 'follow',
        executable = 'follow',
        parameters = [config]
    )

    human_detection_v2=Node(
        package = 'bunker_vis',
        name = 'gesture',
        executable = 'gesture',
        parameters = [config]
    )

    
    # ld.add_action(human_detection)
    ld.add_action(human_detection_v2)
    # ld.add_action(navigation_launch)


    return ld

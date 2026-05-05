from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    rtabmap_launch = PathJoinSubstitution(
        [FindPackageShare("rtabmap_launch"),
        "launch",
        "rtabmap.launch.py"],
    )

    rtbamap_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([rtabmap_launch]),
        launch_arguments={
            'rtabmap_viz': 'false',
            'args' : '--delete_db_on_start',
            'use_sim_time': 'false',
            'queue_size': '100',
            # 'wait_for_transform': '0.5',
            'frame_id': 'base_link',
            'ground_truth_base_frame_id': 'base_link',
            # 'odom_frame_id': 'odom', #if set, TF is used instead of the topic
            'map_frame_id': 'map',
            'publish_tf_map': 'true',
            'subscribe_depth': 'true',
            # 'rgbd_sync': 'true',
            'approx_sync': 'true',
            'approx_sync_max_interval': '0.0',
            'rgb_topic': '/rgb/image_raw',
            'depth_topic': '/depth_to_rgb/image_raw',
            'camera_info_topic': '/rgb/camera_info',
            'subscribe_scan_cloud': 'false',
            # 'scan_cloud_topic': '/velodyne_points',
            'visual_odometry': 'true',
            'icp_odometry': 'false',    
            'stereo': 'false', 
            # 'namespace': '', 
            # 'odom_topic': '/local',   #topic name and frame id for odom
            # 'publish_tf_odom': 'true' ,  
            'imu_topic': '/no_imu',   
            # 'gps_topic': '/gps/fix',   
        }.items(),
    )

    ld = LaunchDescription()
    ld.add_action(rtbamap_sim)

    return ld

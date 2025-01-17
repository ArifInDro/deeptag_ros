from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
             package='deeptag_ros', executable='deep_tag.py', output='screen',
         )
    ])

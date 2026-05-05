#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "nav2_msgs/action/navigate_to_pose.hpp"
#include "map_service/srv/stop_goal.hpp"

#include <memory>

void add(const std::shared_ptr<map_service::srv::StopGoal::Request> request,
          std::shared_ptr<map_service::srv::StopGoal::Response>  response)
    { if (request->data == true) {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request to stop: True"
                    );
        std::shared_ptr<rclcpp::Node> node1 = rclcpp::Node::make_shared("stop_goal");
        rclcpp_action::Client<nav2_msgs::action::NavigateToPose>::SharedPtr cancel_navto_client = 
        rclcpp_action::create_client<nav2_msgs::action::NavigateToPose>(node1,"/navigate_to_pose");
        auto result = cancel_navto_client->async_cancel_all_goals();
  // Wait for the result.
      if (rclcpp::spin_until_future_complete(node1, result) ==
        rclcpp::FutureReturnCode::SUCCESS)
      {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Cancel goal");
      } else {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Failed to cancel goal");
      }
            response->success = true;
    
    }
    else {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request to stop: False"
                    );
        response->success = false;
    
    }
  
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("stop_goal_server");

  rclcpp::Service<map_service::srv::StopGoal>::SharedPtr service =
    node->create_service<map_service::srv::StopGoal>("stop_goal_server", &add);

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to receive stop command.");

  rclcpp::spin(node);
  rclcpp::shutdown();
}
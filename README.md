# Self-Supervised Traversability Learning for Risk-Aware Robot Navigation

## 🚀 Overview
This project focuses on building a learning-based navigation system for mobile robots operating in unstructured environments.  
Instead of relying on hand-engineered costmaps, the robot learns terrain traversability and risk from its own interaction experience.

The system is being developed and validated using the **AgileX BUNKER robot platform** in simulation.

---
<img width="608" height="801" alt="image" src="https://github.com/user-attachments/assets/49e8f032-63cc-49ee-bce0-9c48b31902e6" />

## 🧠 Key Idea
Traditional navigation systems assign fixed costs to terrain.  
This project aims to replace that with:

- Learned traversability from robot experience
- Risk-aware path planning
- Adaptive behavior in complex terrain

---

## 🏗️ System Architecture

- **Robot Platform:** AgileX BUNKER (tracked robot)
- **Framework:** ROS2 (Nav2 stack)
- **Simulation:** NVIDIA Isaac Sim, Gazebo
- **Sensors:**
  - LiDAR
  - RGB-D Camera
  - IMU
- **Learning Approach:** Self-supervised terrain understanding (in progress)

---

## ⚙️ Current Implementation

- ROS2 workspace setup for BUNKER robot
- URDF/xacro modeling adapted for simulation environments
- Sensor integration (LiDAR + RGB-D + IMU)
- Full TF tree configuration
- Nav2 navigation pipeline setup
- Simulation testing in Isaac Sim and Gazebo

---

## 🛠️ My Contributions

- Designed and adapted URDF/xacro models for the BUNKER robot
- Ported and modified robot description from Unity/URDF references for compatibility with NVIDIA Isaac Sim
- Integrated and validated multi-sensor setup (LiDAR, RGB-D, IMU)
- Configured ROS2 Nav2 navigation stack for simulation-based testing
- Performed iterative testing and tuning of robot behavior in Isaac Sim Lab
- Built and maintained full ROS2 workspace for navigation and simulation experiments


## 📊 Future Work

- Self-supervised traversability learning model
- Risk-aware costmap integration in Nav2
- Simulation-to-real transfer
- Deployment on physical BUNKER robot

---

## 🎯 Goal
Enable safe and intelligent navigation for robots operating in challenging terrains such as slopes, loose ground, and rough outdoor environments.

---

## 🧠 Tech Stack
ROS2 • Nav2 • Isaac Sim • Gazebo • LiDAR • RGB-D • IMU • URDF/xacro • SLAM

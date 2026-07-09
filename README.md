# Self-Supervised Traversability Learning for Risk-Aware Robot Navigation

## 🚀 Overview

This master's research project investigates self-supervised traversability learning for autonomous mobile robot navigation in unstructured environments.

Traditional navigation systems rely on manually designed costmaps and heuristic terrain assumptions. This work explores how a robot can learn terrain traversability and navigation risk directly from sensor observations and interaction experience.

The system is being developed using the **AgileX BUNKER tracked robot platform** and validated in simulation before deployment on a physical robot.

---

<p align="center">
  <img src="docs/images/BUNKER_TOPVIEW.png" width="500">
</p>

---

## 🎯 Research Goal

Develop a navigation framework capable of:

* Learning terrain traversability from sensor data
* Estimating navigation risk in unknown environments
* Improving path planning decisions using learned terrain representations
* Transferring learned behavior from simulation to real-world deployment

---

## 🏗️ System Architecture

### Robot Platform

* AgileX BUNKER UGV (Tracked Mobile Robot)

### Software Framework

* ROS2 Humble
* Nav2 Navigation Stack
* RTAB-Map (Planned)
* SLAM Toolbox (Planned)

### Simulation Platforms

* NVIDIA Isaac Sim
* Gazebo

### Sensors

* RTX LiDAR (VLP16-equivalent simulation setup)
* RGB Camera
* Depth Camera
* IMU

### Learning Pipeline

* Self-Supervised Traversability Learning (In Development)
* Risk-Aware Navigation (Planned)

---

## 🔬 Current Progress

### Robot Modeling & Simulation

* [x] BUNKER URDF integration
* [x] Robot import into Isaac Sim
* [x] Sensor mounting and configuration
* [x] ROS2 bridge integration

### Sensor Validation

* [x] LiDAR publishing to ROS2
* [x] RGB camera streaming
* [x] Depth camera streaming
* [x] IMU publishing
* [x] RViz validation of sensor outputs

### Navigation Stack

* [x] TF tree configuration
* [x] Odometry integration
* [x] SLAM integration
* [ ] Nav2 validation

### Learning Pipeline

* [ ] Dataset collection
* [ ] Traversability label generation
* [ ] Self-supervised model training
* [ ] Risk-aware costmap generation
* [ ] Sim-to-real evaluation

---

## 🛠️ Technical Contributions

### Robot Integration

* Adapted and validated BUNKER robot descriptions for simulation environments
* Configured robot assets for NVIDIA Isaac Sim
* Integrated ROS2 communication interfaces

### Sensor Integration

* Configured LiDAR, RGB-D camera, and IMU sensors
* Established ROS2 sensor publishing pipelines
* Validated sensor outputs through RViz visualization

### Simulation Environment

* Built simulation workflows using NVIDIA Isaac Sim
* Conducted sensor testing and validation
* Prepared simulation framework for SLAM and learning experiments

---

## 📂 Repository Structure

```text
docs/
├── progress_logs/
├── images/
├── reports/
└── presentations/

src/
├── bunker_description/
├── bunker_nav/
├── bunker_bringup/
└── simulation/
```

---

## 📊 Future Work

### Navigation

* Configure TF tree and odometry
* Integrate RTAB-Map
* Generate occupancy and elevation maps
* Validate autonomous navigation

### Learning

* Create traversability dataset
* Train self-supervised terrain understanding models
* Integrate learned traversability into Nav2
* Evaluate risk-aware path planning

### Deployment

* Transfer system to physical BUNKER robot
* Validate performance in real-world environments
* Analyze sim-to-real transfer effectiveness

---

## 🧠 Technology Stack

**ROS2 • Nav2 • NVIDIA Isaac Sim • Gazebo • LiDAR • RGB-D • IMU • URDF/Xacro • SLAM • RTAB-Map • Machine Learning**

---

## 📌 Project Status

**Current Phase:** Sensor Integration & Simulation Validation

**Next Milestone:** TF Configuration → Odometry → SLAM Integration → Dataset Collection

---

Developed as part of a Master's research project in autonomous robot navigation and traversability learning.

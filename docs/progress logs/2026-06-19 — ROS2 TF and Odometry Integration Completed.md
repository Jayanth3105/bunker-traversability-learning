# 2026-06-19 — ROS2 TF and Odometry Integration Completed

## Objective

Establish a complete ROS2 TF and odometry pipeline inside Isaac Sim to support future SLAM, localization, and navigation experiments.

---

## Background

Previous sensor validation confirmed successful publication of:

* LiDAR point clouds
* RGB camera images
* Depth images
* IMU data
* Camera calibration information

However, the navigation stack remained incomplete because the required transform between `odom` and `base_link` was not being published.

This prevented RViz, SLAM systems, and navigation frameworks from constructing a complete robot frame hierarchy.

---

## Initial Problem

Odometry messages were successfully published:

```bash
ros2 topic echo /odom --once
```

Output confirmed:

```yaml
frame_id: odom
child_frame_id: base_link
```

However:

```bash
ros2 run tf2_ros tf2_echo odom base_link
```

returned:

```text
Invalid frame ID "odom"
```

RViz also reported:

```text
Frame [odom] does not exist
```

indicating that the odometry message existed but the corresponding TF transform did not.

---

## Existing TF Tree Investigation

Inspection of:

```bash
ros2 topic echo /tf --once
```

showed only sensor transforms:

```text
base_link → body_link
base_link → realsense_D455_link
base_link → xsens_imu_link
base_link → velodyne_VLP16_link
```

The critical transform:

```text
odom → base_link
```

was missing.

---

## Temporary Verification

A temporary static transform was created:

```bash
ros2 run tf2_ros static_transform_publisher \
0 0 0 0 0 0 odom base_link
```

Result:

* RViz accepted `odom` as Fixed Frame
* TF tree became valid

This confirmed that the missing transform was the root cause.

---

## Isaac Sim Graph Modification

A new node was added:

```text
ROS2 Publish Raw Transform Tree
```

Configuration:

```text
Parent Frame Id = odom
Child Frame Id  = base_link
```

Connections:

```text
On Playback Tick
    → Exec In

Isaac Read Simulation Time
    → Timestamp

Isaac Compute Odometry Position
    → Translation

Isaac Compute Odometry Orientation
    → Rotation
```

This enabled Isaac Sim to publish a dynamic transform directly from the computed odometry.

---

## Validation

### Dynamic TF Publication

Verification:

```bash
ros2 topic echo /tf --once
```

Output:

```yaml
frame_id: odom
child_frame_id: base_link
```

---

### Transform Lookup

Verification:

```bash
ros2 run tf2_ros tf2_echo odom base_link
```

Output continuously updated:

```text
Translation: [0.125, 0.000, -0.274]
Translation: [0.335, 0.000, -0.274]
Translation: [0.955, 0.010, -0.264]
Translation: [2.729, 0.151, -0.289]
```

confirming that robot motion was correctly reflected in the TF tree.

---

### Odometry Validation

Robot movement through joystick control produced:

* Continuous position updates
* Continuous orientation updates
* Consistent odometry publication

Pipeline verified:

```text
Joystick
    ↓
cmd_vel
    ↓
Differential Drive Controller
    ↓
Robot Motion
    ↓
Isaac Compute Odometry
    ↓
ROS2 Publish Odometry
    ↓
odom → base_link TF
```

---

## Current TF Tree

```text
odom
 └── base_link
      ├── body_link
      ├── realsense_D455_link
      ├── xsens_imu_link
      └── velodyne_VLP16_link
```

This matches the structure required by:

* RTAB-Map
* SLAM Toolbox
* Nav2
* robot_localization

---

## Remaining Observation

The transform reports:

```text
z ≈ -0.289 m
```

for:

```text
odom → base_link
```

Although `base_link` appears correctly positioned inside Isaac Sim, the odometry computation introduces a vertical offset.

Potential causes:

* Articulation root offset
* Physics root transform
* USD import origin mismatch

This does not currently prevent SLAM operation and will be investigated later.

---

## Session Outcome

### Completed

* [x] ROS2 Odometry Publication
* [x] Dynamic odom → base_link TF
* [x] Sensor TF Hierarchy
* [x] RViz Fixed Frame Validation
* [x] Motion Tracking Validation
* [x] TF Lookup Verification

### Pending

* [ ] Investigate base_link vertical offset
* [ ] RTAB-Map Integration
* [ ] Mapping Validation
* [ ] Loop Closure Testing

---

## Status

The Isaac Sim platform now provides:

* LiDAR
* RGB Camera
* Depth Camera
* IMU
* TF Tree
* Odometry

in a SLAM-ready configuration.

The project can now proceed to RTAB-Map integration and map generation experiments.

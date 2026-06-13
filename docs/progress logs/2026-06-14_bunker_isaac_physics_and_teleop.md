# Progress Log — 2026-06-14

## Completed

### Differential Drive Setup

- Replaced track physics with 4 hidden spherical drive wheels.
- Retained visual track meshes for appearance.
- Configured Isaac Differential Controller for skid-steer locomotion.
- Verified forward, reverse and in-place rotation.

### Wheel Configuration

- Wheel radius: `0.16 m`
- Wheel separation: `0.55 m`

Reason:
- Stable contact behaviour in Isaac Sim.
- Approximates BUNKER track geometry.
- Supports obstacle traversal experiments.

### Physics Tuning

Updated body physics:

| Parameter | Before | After |
|------------|---------|---------|
| Mass | 30 kg | 140 kg |
| Linear Damping | 0 | 0.2 |
| Angular Damping | 0.05 | 0.5 |
| Max Angular Velocity | 5729 | 30 |

Reason:
- Target total robot mass ≈ 150 kg.
- Reduce unrealistic acceleration.
- Improve stability.

### Wheel Joint Tuning

Applied to all wheel joints:

| Parameter | Value |
|------------|---------|
| Drive Type | Acceleration |
| Max Force | 1000 |
| Damping | 300 |
| Stiffness | 0 |

Reason:
- Improve traction and steering response.
- Better match heavy skid-steer behaviour.

### Differential Controller

| Parameter | Value |
|------------|---------|
| Wheel Radius | 0.16 |
| Wheel Distance | 0.55 |
| Max Wheel Speed | 100 |
| Max Linear Speed | 2.0 |
| Max Angular Speed | 3.0 |

### Xbox Teleoperation

Controller mapping:

- LB → Enable
- RB → Turbo

Final teleop parameters:

```yaml
scale_linear.x: 1.5
scale_angular.yaw: 4.0

scale_linear_turbo.x: 2.0
scale_angular_turbo.yaw: 6.0

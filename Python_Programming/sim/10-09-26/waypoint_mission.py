"""Waypoint navigation mission in PX4 OFFBOARD mode."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def send_position(x: float, y: float, z: float) -> None:
    """Send local NED position setpoint."""
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,
        x,
        y,
        z,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    )


def set_offboard_mode() -> None:
    """Switch PX4 to OFFBOARD mode."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0,
        209,  # MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
        6,    # PX4_CUSTOM_MAIN_MODE_OFFBOARD
        0,
        0,
        0,
        0,
        0,
    )


def arm_drone() -> None:
    """Send arm command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1,  # 1 = Arm
        0,
        0,
        0,
        0,
        0,
        0,
    )


# 1. Pre-stream setpoints
print("Preparing OFFBOARD (pre-streaming)...")
for _ in range(50):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 2. Engage OFFBOARD mode without pause
print("Switching to OFFBOARD...")
set_offboard_mode()

for _ in range(10):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 3. Arm drone
print("Arming drone...")
arm_drone()

for _ in range(10):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 4. Climb to initial altitude
print("Climbing to 3m...")
for _ in range(100):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 5. Fly through waypoints
waypoints: list[tuple[float, float, float]] = [
    (0.0, 0.0, -3.0),
    (10.0, 0.0, -3.0),
    (20.0, 5.0, -5.0),
    (10.0, 15.0, -5.0),
    (0.0, 0.0, -3.0),
]

for waypoint in waypoints:
    x, y, z = waypoint
    print(f"Navigating to waypoint: X={x:.1f}, Y={y:.1f}, Z={z:.1f}")
    for _ in range(200):
        send_position(x, y, z)
        time.sleep(0.05)

print("Waypoint mission complete")

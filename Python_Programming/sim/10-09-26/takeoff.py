"""Takeoff to target altitude using PX4 OFFBOARD mode.

Streams position targets to PX4 SITL and ascends to 3m.
"""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def send_position(x: float, y: float, z: float) -> None:
    """Send local NED position target to PX4."""
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,  # Position control mask (ignores vel, acc, yaw)
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
    """Send MAVLink command to switch PX4 into OFFBOARD mode."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0,
        209,  # MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
        6,    # PX4_CUSTOM_MAIN_MODE_OFFBOARD
        0,    # sub_mode
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


# 1. Pre-stream setpoints (PX4 requires setpoint stream BEFORE entering OFFBOARD)
print("Preparing OFFBOARD (pre-streaming 50 setpoints)...")
for _ in range(50):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 2. Switch to OFFBOARD mode without interrupting setpoint stream
print("Switching to OFFBOARD mode...")
set_offboard_mode()

for _ in range(10):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 3. Arm drone while maintaining stream
print("Arming drone...")
arm_drone()

for _ in range(10):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 4. Stream position setpoint to ascend to 3m
print("Taking off to 3m (Z = -3.0)...")
for _ in range(200):
    send_position(0.0, 0.0, -3.0)
    time.sleep(0.05)

print("Takeoff complete: drone at approximately 3m")

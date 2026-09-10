"""Arm PX4 drone motors."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


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


print("Arming...")
arm_drone()
time.sleep(2)
print("Arm command sent")

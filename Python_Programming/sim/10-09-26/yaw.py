"""Control drone heading (yaw) using local NED setpoints."""

import math
import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def send_position_yaw(
    x: float, y: float, z: float, yaw_angle_rad: float
) -> None:
    """Send position target with specific yaw angle to PX4."""
    type_mask = (
        mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
    )
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        type_mask,
        x,
        y,
        z,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        yaw_angle_rad,
        0.0,
    )


# Face 90 degrees (East)
target_yaw: float = math.radians(90.0)
print(f"Setting yaw to 90 degrees ({target_yaw:.2f} rad)...")

for _ in range(200):
    send_position_yaw(0.0, 0.0, -3.0, target_yaw)
    time.sleep(0.05)

print("Yaw target command completed")

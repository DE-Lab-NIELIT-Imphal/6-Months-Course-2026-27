"""PX4 MAVLink helper utilities for offboard control."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")

print("Waiting for heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def send_position(x: float, y: float, z: float) -> None:
    """Send local NED position target to PX4."""
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,  # Ignore velocity, acceleration, and yaw
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


def send_velocity(
    vx: float, vy: float, vz: float, yaw_rate: float = 0.0
) -> None:
    """Send body-frame velocity setpoint to PX4."""
    type_mask = (
        mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE
    )
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        type_mask,
        0.0,
        0.0,
        0.0,
        vx,
        vy,
        vz,
        0.0,
        0.0,
        0.0,
        0.0,
        yaw_rate,
    )


def set_offboard_mode() -> None:
    """Switch PX4 into OFFBOARD mode via MAV_CMD_DO_SET_MODE."""
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


def disarm_drone() -> None:
    """Send disarm command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0,  # 0 = Disarm
        0,
        0,
        0,
        0,
        0,
        0,
    )


def land_drone() -> None:
    """Send land command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LAND,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )


def start_offboard(x: float = 0.0, y: float = 0.0, z: float = -3.0) -> None:
    """Stream setpoints, switch to OFFBOARD mode, and arm cleanly."""
    print("Pre-streaming setpoints...")
    for _ in range(50):
        send_position(x, y, z)
        time.sleep(0.05)

    print("Switching to OFFBOARD...")
    set_offboard_mode()

    for _ in range(10):
        send_position(x, y, z)
        time.sleep(0.05)

    print("Arming drone...")
    arm_drone()

    for _ in range(10):
        send_position(x, y, z)
        time.sleep(0.05)


"""
Coordinate System (MAV_FRAME_LOCAL_NED):
+X = North / Forward
+Y = East / Right
+Z = Down (-Z = Up)

        +X
         ↑
         │
 -Y ←── drone ──→ +Y
         │
         ↓
        -Z = up
"""

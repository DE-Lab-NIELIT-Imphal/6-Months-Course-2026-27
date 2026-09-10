"""Command PX4 drone to Return To Launch (RTL)."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def return_to_launch() -> None:
    """Send Return To Launch (RTL) command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )


print("Switching to RTL...")
return_to_launch()
time.sleep(10)
print("RTL command sent")

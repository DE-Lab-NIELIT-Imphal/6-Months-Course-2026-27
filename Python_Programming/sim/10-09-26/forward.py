"""Move drone forward 10m in local NED frame."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def send_position(x: float, y: float, z: float) -> None:
    """Send local NED position setpoint to drone."""
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


# Send target position (X=10m forward)
print("Moving 10m forward...")
for _ in range(400):
    send_position(10.0, 0.0, -3.0)
    time.sleep(0.05)

print("10m forward target reached")

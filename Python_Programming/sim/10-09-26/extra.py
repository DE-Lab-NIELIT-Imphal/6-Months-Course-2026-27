"""Continuous OFFBOARD setpoint stream with ACK verification."""

import time
from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for heartbeat...")
drone.wait_heartbeat()
print(
    f"Connected: system={drone.target_system}, "
    f"component={drone.target_component}"
)


def send_position_setpoint(x: float, y: float, z: float) -> None:
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
    """Request PX4 OFFBOARD custom mode 6."""
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
    """Arm the drone motors."""
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


# 1. Pre-stream setpoints (PX4 requires setpoint stream before OFFBOARD)
print("Sending setpoints (pre-stream)...")
for _ in range(50):
    send_position_setpoint(0.0, 0.0, -3.0)
    time.sleep(0.05)

# 2. Switch to OFFBOARD mode
print("Requesting OFFBOARD...")
set_offboard_mode()

# 3. Read ACK non-blockingly while continuing setpoint stream (avoids timeout)
ack_received = False
for _ in range(20):
    send_position_setpoint(0.0, 0.0, -3.0)
    time.sleep(0.05)
    ack = drone.recv_match(type="COMMAND_ACK", blocking=False)
    if ack and not ack_received:
        print("COMMAND_ACK received:", ack)
        ack_received = True

# 4. Arm drone while maintaining stream
print("Arming drone...")
arm_drone()

# 5. Continuous setpoint loop
print("Continuing setpoint stream (press Ctrl+C to stop)...")
try:
    while True:
        send_position_setpoint(0.0, 0.0, -3.0)
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nStream stopped by user.")

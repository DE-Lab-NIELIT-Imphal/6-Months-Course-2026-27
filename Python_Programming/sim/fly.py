# from pymavlink import mavutil
# import time

# # 1. Connect to the drone (Update this path to your serial port or UDP address)
# connection = mavutil.mavlink_connection("udp:0.0.0.0:14550")

# print("Waiting for heartbeat...")
# connection.wait_heartbeat()
# print(f"Connected to System {connection.target_system}")

# # 2. Set mode to GUIDED (Required for autonomous commands in ArduPilot)
# # For PX4, you would typically use OFFBOARD mode instead
# print("Switching to GUIDED mode...")
# connection.mav.command_long_send(
#     connection.target_system,
#     connection.target_component,
#     mavutil.mavlink.MAV_CMD_DO_SET_MODE,
#     0,
#     mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
#     4,  # Mode 4 corresponds to GUIDED in ArduPilot
#     0,
#     0,
#     0,
#     0,
#     0,
# )

# # 3. Arm the motors
# print("Arming the drone...")
# connection.mav.command_long_send(
#     connection.target_system,
#     connection.target_component,
#     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
#     0,
#     1,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
# )
# connection.motors_armed_wait()
# print("Drone armed!")

# # 4. Takeoff to exactly 3 meters
# target_altitude = 3.0
# print(f"Taking off to {target_altitude} meters...")
# connection.mav.command_long_send(
#     connection.target_system,
#     connection.target_component,
#     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     target_altitude,
# )

# # Keep the connection alive while it hovers
# time.sleep(10)

# --------------------------------------------------------------------
from pymavlink import mavutil
import time

# Connect to PX4 SITL
drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")

print("Waiting for heartbeat...")
drone.wait_heartbeat()
print("Connected!")

# Send 3m position setpoints before OFFBOARD
for _ in range(100):
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,          # position only
        10, 0, -3,      # X, Y, Z = 3m up
        0, 0, 0,
        0, 0, 0,
        0, 0
    )
    time.sleep(0.05)

# OFFBOARD
drone.set_mode("OFFBOARD")

# ARM
drone.mav.command_long_send(
    drone.target_system,
    drone.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0
)

print("Armed - flying to 3m")

# Hold 3m
while True:
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,
        10, 0, -3,
        0, 0, 0,
        0, 0, 0,
        0, 0
    )
    time.sleep(0.05)
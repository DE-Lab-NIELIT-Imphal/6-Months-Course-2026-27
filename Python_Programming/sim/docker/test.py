# from pymavlink import mavutil

# try:
#     connection_string = mavutil.mavlink_connection('udp:0.0.0.0:14550')
#     print("Connected successfully")

# except:
#     print("Unable to connect")

from pymavlink import mavutil

master = mavutil.mavlink_connection("udp:0.0.0.0:14540")

print("Waiting for PX4 heartbeat...")
master.wait_heartbeat()

print(f"Connected: system={master.target_system}, component={master.target_component}")

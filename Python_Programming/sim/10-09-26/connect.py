from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")

print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()

print("Connected!")
print("System:", drone.target_system)
print("Component:", drone.target_component)

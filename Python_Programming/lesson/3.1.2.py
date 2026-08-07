# Data Types and Variables

drone_id = "UAV-047" # String variable representing the drone's unique identifier
firmware_var = 3.12 # Float variable representing the firmware version of the drone
battery_cells = 4 # Integer variable representing the number of battery cells in the drone
is_armed = False # Boolean variable indicating whether the drone is armed or not
gps_coordinates = (37.7749, -122.4194) # Tuple variable representing the GPS coordinates of the drone's current location
payload_types = ["Camera", "Lidar", "Thermal Sensor"] # List variable representing the types of payloads the drone can carry
sensor_status = {
    "imu": True, # Inertial Measurement Unit
    "gps": True,
    "barometer": False,
    "magnetometer": True
} # Dictionary variable representing the status of various sensors on the drone 

print(f"Drone ID: {drone_id} running firmware version: {firmware_var}")
print(f"Home coordinates: Lat:{gps_coordinates[0]}, Long:{gps_coordinates[1]}")
print(f"Armed status: {is_armed}, Battery cells: {battery_cells}")
print(f"Payload types: {payload_types}")
print(f"Sensor status: {sensor_status}")
# PARAMETERS & ARGUMENTS — Drone Examples


# 1. POSITIONAL
def fly_to(latitude, longitude, altitude):
    print(f"Flying to ({latitude}, {longitude}) at {altitude}m")


fly_to(24.817, 93.944, 50)


# 2. DEFAULT
def arm_drone(drone_id, mode="STABILIZE"):
    print(f"[{drone_id}] Armed in {mode} mode")


arm_drone("UAV-047")  # uses default
arm_drone("UAV-047", "AUTO")  # overrides default


# 3. KEYWORD
def set_altitude(target, speed):
    print(f"Climbing to {target}m at {speed}m/s")


set_altitude(speed=2.5, target=100)  # order doesn't matter


# 4. *args
def load_waypoints(*waypoints):
    print(f"Loaded {len(waypoints)} waypoints: {waypoints}")


load_waypoints((24.81, 93.94), (24.82, 93.95), (24.83, 93.96))


# 5. **kwargs
def log_telemetry(**data):
    for key, value in data.items():
        print(f"  {key}: {value}")


log_telemetry(battery=74, altitude=48, mode="AUTO")

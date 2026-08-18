# declaring a dictionary
vehicle_state = {"battery_pct": 78, "altitude_m": 12.4, "mode": "GUIDED"}
print("Original state: \n", vehicle_state)

print("-" * 100)


# add a new key
vehicle_state["armed"] = True
print("Updated state after addition of a new key: \n", vehicle_state)

print("-" * 100)

# safe lookup, default if missing
battery = vehicle_state.get("battery_pct", 0)
print("Check battery: \n", battery)

print("-" * 100)

# remove & return a key's value
old_mode = vehicle_state.pop("mode")
print("Checking the removed mode: \n", old_mode)
print("Updated state: \n", vehicle_state)

print("-" * 100)

# add a key only if it isn't there yet
vehicle_state.setdefault("gps_fix", False)
print("Updated vehicle state: \n", vehicle_state)

print("-" * 100)

# bulk-update multiple keys at once
vehicle_state.update({"altitude_m": 13.0, "yaw": 88})
print("Vehicle state after bulk update: \n", vehicle_state)

print("-" * 100)

# every field name currently tracked
print("Show all the keys: \n", list(vehicle_state.keys()))
print("-" * 100)

# every current value
print("Show all the values: \n", list(vehicle_state.values()))
print("-" * 100)

# iterate name/value pairs together
print("Key \t  Value")
for key, value in vehicle_state.items():
    print(f"{key}: {value}")

print("-" * 100)

# shallow copy, e.g. before a risky command
backup_state = vehicle_state.copy()
print("Backing up state and preview: \n", backup_state)

print("-" * 100)

# remove the most-recently-added pair
last_key, last_val = vehicle_state.popitem()
print("Deleting the pair:\n", last_key, last_val)
print("Updated vehicle state: \n", vehicle_state)

print("-" * 100)

# reset entirely once the drone has landed
vehicle_state.clear()
print("Clearing all the state: \n", vehicle_state)
print("-" * 100)

print(backup_state)
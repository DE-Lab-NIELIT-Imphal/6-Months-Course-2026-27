# Control structures - selection

# altitude_m   = 87
# wind_speed   = 22          # km/h
# battery_pct  = 18

# if battery_pct < 20:
#     flight_mode = "RTL"    # Return to Launch
#     print(f"⚠ Low battery ({battery_pct}%) — initiating RTL")
# elif wind_speed > 40:
#     flight_mode = "HOLD"
#     print(f"⚠ High wind ({wind_speed} km/h) — switching to HOLD")
# elif altitude_m > 120:
#     flight_mode = "DESCEND"
#     print(f"⚠ Altitude limit exceeded — descending")
# else:
#     flight_mode = "AUTO"
#     print(f"✓ Conditions nominal — AUTO mission active")

# for loop demo
waypoints = [
    {"id": 1, "lat": 24.817, "lon": 93.944, "alt": 50},
    {"id": 2, "lat": 24.820, "lon": 93.948, "alt": 50},
    {"id": 3, "lat": 24.823, "lon": 93.951, "alt": 30},
]

print("\n── Mission Log ──")
for wp in waypoints:
    print(
        f"  Navigating to WP{wp['id']} → " f"({wp['lat']}, {wp['lon']}) at {wp['alt']}m"
    )

# while loop demo
import time

satellites_locked = 0
required_sats = 6

print("\n── Acquiring GPS Lock ──")
while satellites_locked < required_sats:
    satellites_locked += 1  # simulates satellite acquisition
    print(f"  Satellites: {satellites_locked}/{required_sats}")
    time.sleep(5)                 # uncomment for real timing

print("✓ GPS lock acquired — ready for autonomous flight\n")

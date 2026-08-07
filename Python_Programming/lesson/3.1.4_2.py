#  BREAK, CONTINUE, PASS — Drone Flight Control Examples

# ── BREAK — Emergency Stop on Critical Fault ───────────────
# Scans telemetry stream; halts immediately on critical error

telemetry_stream = [
    {"tick": 1, "status": "OK", "battery": 85},
    {"tick": 2, "status": "OK", "battery": 83},
    {"tick": 3, "status": "WARN_WIND", "battery": 82},
    {"tick": 4, "status": "CRITICAL_IMU", "battery": 81},
    {"tick": 5, "status": "OK", "battery": 80},  # never reached
]

print("── Telemetry Monitor ──")
for packet in telemetry_stream:
    print(f"  Tick {packet['tick']} | {packet['status']} | Batt: {packet['battery']}%")

    if packet["status"].startswith("CRITICAL"):
        print(f"  ✖ CRITICAL FAULT DETECTED — killing motors & exiting loop")
        break  # stop scanning; trigger failsafe immediately

print()


# ── CONTINUE — Skip Blocked/No-Fly Waypoints ──────────────
# Iterates mission plan; skips any waypoint flagged as restricted

mission_waypoints = [
    {"id": 1, "lat": 24.817, "lon": 93.944, "restricted": False},
    {"id": 2, "lat": 24.820, "lon": 93.948, "restricted": True},  # no-fly zone
    {"id": 3, "lat": 24.823, "lon": 93.951, "restricted": False},
    {"id": 4, "lat": 24.826, "lon": 93.955, "restricted": True},  # no-fly zone
    {"id": 5, "lat": 24.829, "lon": 93.959, "restricted": False},
]

print("── Mission Execution ──")
for wp in mission_waypoints:
    if wp["restricted"]:
        print(f"  ⚠ WP{wp['id']} is in a restricted zone — skipping")
        continue  # jump to next waypoint; don't execute flight command

    print(f"  ✓ Flying to WP{wp['id']} → ({wp['lat']}, {wp['lon']})")

print()


# ── PASS — Stubbed Flight Mode Handlers ───────────────────
# Defines all flight modes upfront; unimplemented ones use pass
# as a placeholder so the structure runs without errors

flight_mode = "LOITER"

print(f"── Flight Mode Handler: {flight_mode} ──")

if flight_mode == "AUTO":
    print("  Executing autonomous waypoint mission")

elif flight_mode == "RTL":
    print("  Returning to launch point")

elif flight_mode == "LOITER":
    pass  # TODO: implement position-hold PID logic
    # drone holds position silently for now

elif flight_mode == "GUIDED":
    pass  # TODO: implement GCS command relay

elif flight_mode == "LAND":
    pass  # TODO: implement precision landing sequence

print(f"  Mode '{flight_mode}' handler registered (some pending implementation)")

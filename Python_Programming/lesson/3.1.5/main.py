# main function putting altogether the preflight checks and mission execution

from preflight import run_preflight
from mission import run_mission


def main():
    print("══════════════════════════════════")
    print("   UAV-047  |  PRE-FLIGHT SYSTEM  ")
    print("══════════════════════════════════\n")

    voltage = 15.4
    satellites = 8
    sensors = {
        "IMU": True,
        "Barometer": True,
        "Magnetometer": True,  # ← fixed
        "GPS Module": True,
    }

    waypoints = [
        {"id": 1, "lat": 24.817, "lon": 93.944, "alt": 50, "restricted": False},
        {"id": 2, "lat": 24.820, "lon": 93.948, "alt": 50, "restricted": True},
        {"id": 3, "lat": 24.823, "lon": 93.951, "alt": 40, "restricted": False},
        {"id": 4, "lat": 24.827, "lon": 93.956, "alt": 30, "restricted": False},
    ]

    print("── Preflight Report ──")
    ready, report = run_preflight(voltage, satellites, sensors)
    for line in report:
        print(line)

    print(f"\n  Status: {'✓ ARMED — Launching' if ready else '✖ NOT READY — Abort'}")

    if ready:
        run_mission(waypoints)
    else:
        print("  Mission aborted. Fix faults and retry.\n")


if __name__ == "__main__":
    main()

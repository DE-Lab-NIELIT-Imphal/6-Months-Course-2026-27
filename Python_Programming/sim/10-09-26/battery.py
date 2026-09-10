"""Read battery status from PX4."""

from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def read_battery() -> None:
    """Continuously receive and display battery status."""
    print("Reading battery status (Ctrl+C to stop)...")
    try:
        while True:
            msg = drone.recv_match(type="SYS_STATUS", blocking=True)
            if msg:
                print(f"Battery: {msg.battery_remaining}%")
    except KeyboardInterrupt:
        print("\nBattery reader stopped.")


if __name__ == "__main__":
    read_battery()

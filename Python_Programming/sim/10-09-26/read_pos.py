"""Read drone local NED position from PX4."""

from pymavlink import mavutil

drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
print("Waiting for PX4 heartbeat...")
drone.wait_heartbeat()
print(f"Connected to PX4 (System ID: {drone.target_system})")


def read_position() -> None:
    """Continuously receive and display LOCAL_POSITION_NED messages."""
    print("Reading position (Ctrl+C to stop)...")
    try:
        while True:
            msg = drone.recv_match(type="LOCAL_POSITION_NED", blocking=True)
            if msg:
                print(
                    f"X: {msg.x:.2f} m | Y: {msg.y:.2f} m | Z: {msg.z:.2f} m"
                )
    except KeyboardInterrupt:
        print("\nPosition reader stopped.")


if __name__ == "__main__":
    read_position()

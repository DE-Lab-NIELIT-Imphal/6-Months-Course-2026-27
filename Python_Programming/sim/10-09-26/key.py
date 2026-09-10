"""PX4 SITL Keyboard Control with Takeoff & Velocity Navigation.

Controls a PX4 drone via velocity setpoints in OFFBOARD mode.
Supports automated takeoff via position setpoints and manual flight control.
Uses msvcrt on Windows and termios/tty on Unix for non-blocking input.
"""

import sys
import time
from pymavlink import mavutil

# --------------------------------------------------
# Cross-platform non-blocking keyboard input
# --------------------------------------------------
IS_WINDOWS: bool = sys.platform == "win32"

if IS_WINDOWS:
    import msvcrt

    def init_keyboard() -> None:
        """Initialize keyboard input on Windows (no-op)."""
        pass

    def cleanup_keyboard() -> None:
        """Restore keyboard input on Windows (no-op)."""
        pass

    def get_key() -> str | None:
        """Read a non-blocking keypress on Windows."""
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            # Handle 2-byte prefix for arrow and special keys
            if ch in (b"\x00", b"\xe0"):
                ch = msvcrt.getch()
            return ch.decode("utf-8", errors="ignore").lower()
        return None

else:
    import select
    import termios
    import tty

    _old_settings = None

    def init_keyboard() -> None:
        """Set terminal to cbreak mode on Unix/Linux/macOS."""
        global _old_settings
        _old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def cleanup_keyboard() -> None:
        """Restore terminal settings on Unix/Linux/macOS."""
        if _old_settings is not None:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, _old_settings)

    def get_key() -> str | None:
        """Read a non-blocking keypress on Unix/Linux/macOS."""
        if select.select([sys.stdin], [], [], 0)[0]:
            return sys.stdin.read(1).lower()
        return None


# --------------------------------------------------
# MAVLink Control & Setpoints
# --------------------------------------------------
def send_position(
    drone: mavutil.mavfile,
    x: float,
    y: float,
    z: float,
) -> None:
    """Send local NED position setpoint to PX4."""
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        3576,  # Ignore velocity, acceleration, and yaw
        x,
        y,
        z,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    )


def send_velocity(
    drone: mavutil.mavfile,
    vx: float,
    vy: float,
    vz: float,
    yaw_rate: float,
) -> None:
    """Send body-frame velocity setpoint to PX4."""
    type_mask = (
        mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE
        | mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE
    )
    drone.mav.set_position_target_local_ned_send(
        0,
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        type_mask,
        0.0,
        0.0,
        0.0,
        vx,
        vy,
        vz,
        0.0,
        0.0,
        0.0,
        0.0,
        yaw_rate,
    )


def set_offboard_mode(drone: mavutil.mavfile) -> None:
    """Command PX4 into OFFBOARD mode (main_mode=6)."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0,
        209,  # MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
        6,    # PX4_CUSTOM_MAIN_MODE_OFFBOARD
        0,
        0,
        0,
        0,
        0,
    )


def arm_drone(drone: mavutil.mavfile) -> None:
    """Send arm command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
    )


def land_drone(drone: mavutil.mavfile) -> None:
    """Send land command to PX4."""
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LAND,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )


def perform_takeoff(
    drone: mavutil.mavfile,
    altitude: float = 2.5,
    duration_s: float = 4.0,
) -> None:
    """Ascend to target altitude using position setpoints."""
    print(f"\n[TAKEOFF] Ascending to {altitude:.1f}m...")
    target_z: float = -abs(altitude)
    steps: int = int(duration_s / 0.05)
    for _ in range(steps):
        send_position(drone, 0.0, 0.0, target_z)
        time.sleep(0.05)
    print(f"[TAKEOFF] Reached {altitude:.1f}m. Hovering in OFFBOARD mode.\n")


def start_offboard_stream(
    drone: mavutil.mavfile,
    auto_takeoff: bool = True,
) -> None:
    """Pre-stream setpoints, switch to OFFBOARD, arm, and perform takeoff."""
    target_z: float = -2.5
    print("Preparing OFFBOARD (pre-streaming setpoints)...")
    for _ in range(50):
        send_position(drone, 0.0, 0.0, target_z)
        time.sleep(0.05)

    print("Switching to OFFBOARD mode...")
    set_offboard_mode(drone)

    for _ in range(10):
        send_position(drone, 0.0, 0.0, target_z)
        time.sleep(0.05)

    print("Arming drone...")
    arm_drone(drone)

    for _ in range(10):
        send_position(drone, 0.0, 0.0, target_z)
        time.sleep(0.05)

    if auto_takeoff:
        perform_takeoff(drone, altitude=2.5, duration_s=4.0)


def print_instructions() -> None:
    """Display user controls."""
    print("=" * 36)
    print("       PX4 KEYBOARD CONTROL")
    print("=" * 36)
    print("T   : Takeoff (climb to 2.5m)")
    print("W/S : Forward / Backward (+/- 2.0 m/s)")
    print("A/D : Left / Right       (+/- 2.0 m/s)")
    print("R/F : Up / Down          (+/- 1.5 m/s)")
    print("Q/E : Yaw Left / Right   (+/- 0.5 rad/s)")
    print("L   : Land and Exit")
    print("X   : Exit")
    print("=" * 36)
    print("Press any movement key to steer...\n")


def parse_key_command(
    key: str | None,
) -> tuple[float, float, float, float, bool, bool, bool]:
    """Parse pressed key into velocity setpoints and control flags.

    Returns: (vx, vy, vz, yaw_rate, should_takeoff, should_land, should_exit)
    """
    if not key:
        return 0.0, 0.0, 0.0, 0.0, False, False, False

    if key == "t":
        return 0.0, 0.0, 0.0, 0.0, True, False, False
    if key == "w":
        return 2.0, 0.0, 0.0, 0.0, False, False, False
    if key == "s":
        return -2.0, 0.0, 0.0, 0.0, False, False, False
    if key == "a":
        return 0.0, -2.0, 0.0, 0.0, False, False, False
    if key == "d":
        return 0.0, 2.0, 0.0, 0.0, False, False, False
    if key == "r":
        return 0.0, 0.0, -1.5, 0.0, False, False, False
    if key == "f":
        return 0.0, 0.0, 1.5, 0.0, False, False, False
    if key == "q":
        return 0.0, 0.0, 0.0, -0.5, False, False, False
    if key == "e":
        return 0.0, 0.0, 0.0, 0.5, False, False, False
    if key == "l":
        return 0.0, 0.0, 0.0, 0.0, False, True, False
    if key == "x":
        return 0.0, 0.0, 0.0, 0.0, False, False, True

    return 0.0, 0.0, 0.0, 0.0, False, False, False


def run_control_loop(drone: mavutil.mavfile) -> None:
    """Continuously poll keyboard and stream velocity setpoints."""
    print_instructions()
    while True:
        key = get_key()
        vx, vy, vz, yaw, do_takeoff, do_land, do_exit = parse_key_command(key)

        if do_takeoff:
            perform_takeoff(drone, altitude=2.5, duration_s=3.0)
            continue

        if do_land:
            print("\nLanding drone...")
            land_drone(drone)
            break

        if do_exit:
            print("\nExiting controller...")
            break

        send_velocity(drone, vx, vy, vz, yaw)
        time.sleep(0.05)


def main() -> None:
    """Connect to PX4, engage offboard, and start control loop."""
    drone = mavutil.mavlink_connection("udp:127.0.0.1:14540")
    print("Waiting for PX4 heartbeat...")
    drone.wait_heartbeat()
    print(f"Connected to PX4 (System ID: {drone.target_system})")

    init_keyboard()
    try:
        start_offboard_stream(drone, auto_takeoff=True)
        run_control_loop(drone)
    finally:
        for _ in range(20):
            send_velocity(drone, 0.0, 0.0, 0.0, 0.0)
            time.sleep(0.05)
        cleanup_keyboard()
        print("Controller stopped.")


if __name__ == "__main__":
    main()

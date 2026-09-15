from pymavlink import mavutil
import time

# CONNECTION = "/dev/ttyACM0"
CONNECTION = "COM9"
BAUD = 115200

print(f"Connecting to Pixhawk on {CONNECTION} ...")
mav = mavutil.mavlink_connection(CONNECTION, baud=BAUD)

print("Waiting for heartbeat ...")
mav.wait_heartbeat()
print(
    f"Heartbeat received  |  system={mav.target_system}  "
    f"component={mav.target_component}"
)

mav.mav.request_data_stream_send(
    mav.target_system,
    mav.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_ALL,
    4,  # 4 Hz
    1,  # start streaming
)

MESSAGES = ["HEARTBEAT", "ATTITUDE", "SYS_STATUS", "GPS_RAW_INT"]

print("\n-- Live Telemetry (Ctrl+C to stop) -------------------------------")
try:
    while True:
        msg = mav.recv_match(type=MESSAGES, blocking=True, timeout=2)
        if msg is None:
            continue

        t = msg.get_type()

        if t == "HEARTBEAT":
            armed = "ARMED" if msg.base_mode & 128 else "DISARMED"
            print(f"[HEARTBEAT]  system_status={msg.system_status}  {armed}")

        elif t == "ATTITUDE":
            print(
                f"[ATTITUDE ]  roll={msg.roll:+.3f} rad  "
                f"pitch={msg.pitch:+.3f} rad  yaw={msg.yaw:+.3f} rad"
            )

        elif t == "SYS_STATUS":
            voltage = msg.voltage_battery / 1000.0
            print(
                f"[SYS_STATUS]  battery={voltage:.2f} V  "
                f"cpu_load={msg.load / 10.0:.1f} %"
            )

        elif t == "GPS_RAW_INT":
            print(
                f"[GPS      ]  fix={msg.fix_type}  "
                f"satellites={msg.satellites_visible}"
            )

except KeyboardInterrupt:
    print("\nStopped by user.")

# PX4 SITL Drone Control with Pymavlink

A structured curriculum and collection of Python scripts for controlling a PX4 drone in SITL (Software In The Loop) simulation using `pymavlink` over MAVLink (`udp:127.0.0.1:14540`).

---

## Coordinate Frame (MAV_FRAME_LOCAL_NED)

All local position and velocity setpoints use the **NED** (North-East-Down) convention:

```text
        +X (Forward / North)
         ↑
         │
-Y ←── Drone ──→ +Y (Right / East)
(Left)   │
         ↓
        +Z (Down)  -->  -Z is UP (e.g., -3m = 3m altitude)
```

---

## Script Flow & Descriptions

| # | Script | Description |
|---|---|---|
| 1 | [connect.py](connect.py) | Connects to PX4 SITL and prints System/Component IDs after receiving a heartbeat. |
| 2 | [arm.py](arm.py) | Sends `MAV_CMD_COMPONENT_ARM_DISARM` to arm the motors. |
| 3 | [takeoff.py](takeoff.py) | Pre-streams setpoints at 20 Hz, engages `OFFBOARD` mode, arms, and climbs to 3m (`Z = -3.0`). |
| 4 | [hover.py](hover.py) | Maintains position hold at `(0, 0, -3)` by continuously streaming position setpoints. |
| 5 | [forward.py](forward.py) | Commands drone forward by 10m (`X = 10, Y = 0, Z = -3`). |
| 6 | [backward.py](backward.py) | Commands drone backward by 10m (`X = -10, Y = 0, Z = -3`). |
| 7 | [right.py](right.py) | Commands drone right by 10m (`X = 0, Y = 10, Z = -3`). |
| 8 | [left.py](left.py) | Commands drone left by 10m (`X = 0, Y = -10, Z = -3`). |
| 9 | [square_mission.py](square_mission.py) | Flies a 10m x 10m square path at 3m altitude in `OFFBOARD` mode. |
| 10 | [waypoint_mission.py](waypoint_mission.py) | Traverses a sequence of 3D waypoints at various altitudes. |
| 11 | [yaw.py](yaw.py) | Commands drone heading to face 90 degrees (East) while holding position. |
| 12 | [read_pos.py](read_pos.py) | Continuously reads and prints `LOCAL_POSITION_NED` telemetry. |
| 13 | [battery.py](battery.py) | Continuously reads and prints battery percentage from `SYS_STATUS`. |
| 14 | [rtl.py](rtl.py) | Triggers Return-To-Launch via `MAV_CMD_NAV_RETURN_TO_LAUNCH`. |
| 15 | [land.py](land.py) | Commands autonomous landing via `MAV_CMD_NAV_LAND`. |
| 16 | [key.py](key.py) | Interactive real-time keyboard flight controller (Windows & Linux compatible). |
| 17 | [extra.py](extra.py) | Example showing non-blocking ACK verification while streaming setpoints. |
| 18 | [assignment.md](assignment.md) | Hands-on lab assignments, flight scenarios, and reference code implementations. |
| -- | [helper.py](helper.py) | Reusable module containing offboard initiation, arming, landing, and stream helpers. |

---

## Keyboard Control (`key.py`)

[key.py](key.py) provides interactive non-blocking control using `msvcrt` on Windows and `termios`/`tty` on Unix.

### Startup Behavior
- Automatically pre-streams setpoints at 20 Hz.
- Switches to `OFFBOARD` mode, arms the vehicle, and executes auto-takeoff to **2.5m**.
- Hands over to manual keyboard velocity control once airborne.

### Control Keys

| Key | Action | Value |
|---|---|---|
| **`T`** | **Takeoff** | Ascends to 2.5m via position setpoints |
| **`W` / `S`** | Forward / Backward | `+2.0` / `-2.0` m/s (`vx`) |
| **`A` / `D`** | Left / Right | `-2.0` / `+2.0` m/s (`vy`) |
| **`R` / `F`** | Up / Down | `-1.5` / `+1.5` m/s (`vz`) |
| **`Q` / `E`** | Yaw Left / Right | `-0.5` / `+0.5` rad/s (`yaw_rate`) |
| **`L`** | Land | Executes `MAV_CMD_NAV_LAND` and exits |
| **`X`** | Exit | Sends zero-velocity stop stream and quits |

---

## Key Offboard Architecture Fixes

1. **Explicit Offboard Mode Command (`MAV_CMD_DO_SET_MODE`)**  
   `drone.set_mode("OFFBOARD")` fails in `pymavlink` because `"OFFBOARD"` is missing from the default mode mapping for PX4. Scripts now use `command_long_send` with `MAV_CMD_DO_SET_MODE` (`param1 = 209`, `param2 = 6`, `param3 = 0`).

2. **Uninterrupted 20 Hz Setpoint Stream (500 ms Rule)**  
   PX4 has a 500 ms timeout (`COM_OF_LOSS_T`). Pausing setpoints (e.g., `time.sleep(1)`) triggers an immediate offboard loss failsafe. All transitions (mode switch, arming, telemetry reads) now maintain continuous setpoint streaming.

3. **Position Setpoints for Takeoff**  
   PX4 ground detector ignores body-velocity climb commands (`vz = -1.5`) while landed. Takeoff must use position setpoints (`send_position` with negative Z) to trigger motor spool-up and lift-off before switching to velocity control.
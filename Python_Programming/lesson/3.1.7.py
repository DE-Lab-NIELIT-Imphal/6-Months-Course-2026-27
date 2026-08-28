# STRING HANDLING

# --- f-strings / formatting ---
altitude = 12.437
battery = 78
log_line = f"[ALT] {altitude:.2f} m | BATTERY {battery:3d}%"
print(log_line)  # [ALT] 12.44 m | BATTERY  78%

padded = f'{"temp":<12}: {24.5:>6.2f} C'  # left/right alignment
print(padded)  # temp        :  24.50 C


# --- split() / join() ---
raw = "TEMP:24.5,HUM:60,DIST:87"
pairs = raw.split(",")  # ['TEMP:24.5', 'HUM:60', 'DIST:87']
parsed = dict(
    p.split(":") for p in pairs
)  # {'TEMP': '24.5', 'HUM': '60', 'DIST': '87'}

fields = ["2026-08-18", "10:14:02", "24.5", "SAFE"]
csv_row = ",".join(fields)  # '2026-08-18,10:14:02,24.5,SAFE'


# --- strip() / lstrip() / rstrip() ---
serial_line = "  ARM:1\r\n"
clean = serial_line.strip()  # 'ARM:1' - removes whitespace/newline junk


# --- replace() ---
command = "SET_MODE:GUIDED"
safe_cmd = command.replace("GUIDED", "LOITER")  # 'SET_MODE:LOITER'


# --- find() / index() ---
telemetry = "HEARTBEAT:OK;BATTERY:78;GPS:FIX"
pos = telemetry.find("BATTERY")  # 13 (returns -1 if not found)
pos2 = telemetry.index("GPS")  # 23 (raises ValueError if not found)


# --- startswith() / endswith() ---
gcs_command = "ARM:1"
if gcs_command.startswith("ARM"):
    print("Arming command received")

log_file = "sensor_log.csv"
if log_file.endswith(".csv"):
    print("Valid log format")


# --- upper() / lower() ---
mode = "guided"
normalized_mode = mode.upper()  # 'GUIDED' - MAVLink modes are uppercase


# --- zfill() ---
mission_id = 7
filename = f"mission_{str(mission_id).zfill(3)}.log"  # 'mission_007.log'


# --- in / not in (membership check) ---
status_text = "ENV UNSAFE: Humidity 82% > 70% limit"
if "UNSAFE" in status_text:
    print("Trigger alert")


# --- encode() / decode() ---
statustext = "ENV OK"
payload = statustext.encode("utf-8")  # b'ENV OK' - bytes, for MAVLink/socket send
message = payload.decode("utf-8")  # 'ENV OK' - back to a string on receive


# --- slicing ---
timestamp = "2026-08-18T10:14:02"
date_part = timestamp[:10]  # '2026-08-18'
time_part = timestamp[11:]  # '10:14:02'

# Raw telemetry log structured as a Python dictionary
telem = [
    {
        "timestamp": "10:00:01",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "altitude_m": 0.0,
        "speed_ms": 0.0,
        "roll_deg": 0.1,
        "pitch_deg": -0.2,
        "yaw_deg": 45.2,
        "battery_pct": 100,
        "satellites": 14,
    },
    {
        "timestamp": "10:00:02",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "altitude_m": 1.2,
        "speed_ms": 1.1,
        "roll_deg": 0.5,
        "pitch_deg": -1.5,
        "yaw_deg": 45.1,
        "battery_pct": 100,
        "satellites": 14,
    },
]

import csv

# Define the CSV headers based on the dictionary keys
fields = list(telem[0].keys())

# Write the data to a CSV file
with open("log.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(telem)
    print("Data logged into log.csv")


with open("log.csv", "r", newline="") as csvfile:
    pass

# Runs all preflight checks before arming
from battery import get_battery_percentage, check_battery_status


def check_gps(satellites):
    """Returns True if GPS lock is sufficient."""
    return satellites >= 6


def check_sensors(sensor_dict):
    """Returns True only if all sensors are healthy."""
    return all(sensor_dict.values())


def run_preflight(voltage, satellites, sensors):
    """
    Master preflight check — calls all sub-checks.
    Returns (is_ready, report_list).
    """
    report = []

    # Battery
    pct = get_battery_percentage(voltage)
    status = check_battery_status(pct)
    report.append(f"  Battery   : {pct}% [{status}]")

    # GPS
    gps_ok = check_gps(satellites)
    report.append(f"  GPS Lock  : {'✓' if gps_ok else '✖'} ({satellites} sats)")

    # Sensors
    sensors_ok = check_sensors(sensors)
    for name, state in sensors.items():
        report.append(f"  {name:<12}: {'✓' if state else '✖'}")

    is_ready = (status != "CRITICAL") and gps_ok and sensors_ok
    return is_ready, report

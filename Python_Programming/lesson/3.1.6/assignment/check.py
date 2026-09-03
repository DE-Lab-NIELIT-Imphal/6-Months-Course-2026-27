def check_drone_armable(
    gps_fix: int, satellites: int, waypoints_loaded: int, battery_voltage: float
) -> tuple[bool, list]:
    """
    Evaluates raw telemetry values to determine if the drone is safe to arm.
    Returns (is_armable: bool, error_list: list).
    """
    errors = []

    if gps_fix < 3:
        errors.append(
            f"Insufficient GPS Fix: Type {gps_fix}. Minimum 3 (3D Fix) required."
        )

    if satellites < 8:
        errors.append(
            f"Low Satellite Count: {satellites}. Minimum 8 required for stable flight."
        )

    if waypoints_loaded == 0:
        errors.append("No waypoints loaded. Mission cannot be executed.")

    if battery_voltage < 14.8:
        errors.append(
            f"Battery voltage critical: {battery_voltage}V. Minimum 14.8V required."
        )

    is_armable = len(errors) == 0
    return is_armable, errors

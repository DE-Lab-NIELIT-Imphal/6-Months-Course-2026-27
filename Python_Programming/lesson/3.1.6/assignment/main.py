from check import check_drone_armable

def evaluate_and_print(drone_id: str, gps_fix: int, satellites: int, waypoints: int, voltage: float):
    print(f"=== PRE-FLIGHT DIAGNOSTICS: {drone_id.upper()} ===")
    
    # Passing raw arguments directly
    armable, issues = check_drone_armable(gps_fix, satellites, waypoints, voltage)
    
    if armable:
        print("[ OK ] STATUS: ARMING APPROVED")
        print("       All checks passed. Ready for takeoff.\n")
    else:
        print("[FAIL] STATUS: ARMING REJECTED")
        for issue in issues:
            print(f"       -> {issue}")
        print()

if __name__ == "__main__":
    # Test Case 1: Failing conditions
    # Arguments: gps_fix, satellites, waypoints_loaded, battery_voltage
    evaluate_and_print("UAV-01", 2, 5, 0, 14.2)

    # Test Case 2: Passing conditions
    evaluate_and_print("UAV-02", 3, 12, 4, 16.0)
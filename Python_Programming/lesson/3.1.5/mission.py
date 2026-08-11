# Handles waypoint navigation logic


def calc_distance(wp1, wp2):
    """Rough flat-earth distance in meters between two waypoints."""
    lat_diff = (wp2["lat"] - wp1["lat"]) * 111_000
    lon_diff = (wp2["lon"] - wp1["lon"]) * 111_000
    return round((lat_diff**2 + lon_diff**2) ** 0.5, 1)


def fly_to(waypoint):
    """Simulates flying to a single waypoint."""
    print(
        f"    → Flying to WP{waypoint['id']} "
        f"({waypoint['lat']}, {waypoint['lon']}) "
        f"at {waypoint['alt']}m"
    )


def run_mission(waypoints):
    """Executes full waypoint mission, logs total distance."""
    print("\n  ── Mission Start ──")
    total_dist = 0

    for i, wp in enumerate(waypoints):
        if wp.get("restricted"):
            print(f"    ⚠ WP{wp['id']} restricted — skipping")
            continue

        fly_to(wp)

        if i > 0:
            total_dist += calc_distance(waypoints[i - 1], wp)

    print(f"  ── Mission Complete | Total distance: {total_dist}m ──")

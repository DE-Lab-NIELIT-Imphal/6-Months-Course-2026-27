# Handles all battery-related checks


def get_battery_percentage(voltage, cells=4, cell_max=4.2, cell_min=3.5):
    """Returns battery % based on current voltage."""
    max_v = cell_max * cells
    min_v = cell_min * cells
    percentage = ((voltage - min_v) / (max_v - min_v)) * 100
    return round(max(0, min(100, percentage)), 1)


def check_battery_status(percentage):
    """Returns battery status label."""
    if percentage > 50:
        return "GOOD"
    elif percentage > 20:
        return "LOW"
    else:
        return "CRITICAL"

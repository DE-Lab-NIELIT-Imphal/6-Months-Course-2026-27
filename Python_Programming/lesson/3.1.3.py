# Operators and Expressions

battery_voltage   = 15.8    # volts (4S pack)
battery_capacity  = 5200    # mAh
current_draw_avg  = 18.5    # amps (hover current)
cell_min_voltage  = 3.5     # volts per cell (cutoff)

is_armed= True

# Arithmetic operators
flight_time_hrs  = (battery_capacity / 1000) / current_draw_avg
flight_time_min  = flight_time_hrs * 60

# Comparison operators
cells            = 4
safe_to_fly      = battery_voltage > (cell_min_voltage * cells)  # True/False

# Logical operators
gps_fix          = True
home_set         = True
ready_to_launch  = is_armed and gps_fix and home_set

# Modulo — check if waypoint index is a return-home checkpoint
waypoint_index   = 9
is_checkpoint    = (waypoint_index % 3 == 0)

print(f"Est. flight time: {flight_time_min:.1f} min")
print(f"Safe voltage: {safe_to_fly} | Launch ready: {ready_to_launch}")
print(f"Waypoint {waypoint_index} is a checkpoint: {is_checkpoint}")

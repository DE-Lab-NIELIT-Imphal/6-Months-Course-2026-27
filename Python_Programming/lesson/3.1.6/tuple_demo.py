mission_waypoints = [
    (28.61, 77.20, 10),  # (lat, lon, alt_m)
    (28.62, 77.21, 15),
    (28.61, 77.20, 10),  # revisits the first waypoint on the way back
]

home = mission_waypoints[0]  # indexing into the list of tuples
lat, lon, alt = home  # unpacking - the most-used tuple skill
first_two_legs = mission_waypoints[0:2]  # slicing still works on tuples inside a list

print(mission_waypoints.count((28.61, 77.20, 10)))  # count() - how many times revisited
print(
    mission_waypoints.index((28.62, 77.21, 15))
)  # index() - locate a specific waypoint

geofence_bounds = (28.55, 28.70, 77.10, 77.30)  # (lat_min, lat_max, lon_min, lon_max)
# geofence_bounds[0] = 28.60      # TypeError - tuples cannot be modified after creation

# Bonus: namedtuple gives fields names instead of positions, while staying immutable
from collections import namedtuple

Waypoint = namedtuple("Waypoint", ["lat", "lon", "alt"])
wp = Waypoint(28.61, 77.20, 10)
print(wp.lat, wp.alt, wp.lon)  # access by name, not by wp[0]/wp[2]


# Write a a python function that checks if a drone is armable, and the function should include checks like satellite, gps fix and waypoints etc. Import this function and use it inside a main.py file and inside that main file, all print statements should be formatted in such a way that a person can easily read the outputs. 
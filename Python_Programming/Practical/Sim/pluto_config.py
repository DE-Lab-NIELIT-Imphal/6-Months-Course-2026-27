from plutocontrol import Pluto

# Create an instance of the Pluto class with default IP (192.168.4.1:23)
pluto = Pluto()

# Connect to the drone
pluto.connect()

# Arm the drone
pluto.arm()

# Disarm the drone
pluto.disarm()

# Disconnect from the drone
pluto.disconnect()

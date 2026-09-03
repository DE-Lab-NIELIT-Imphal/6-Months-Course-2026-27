from plutocontrol import Pluto
import time

my_pluto = Pluto()
my_pluto.connect()

print("Arming...")
my_pluto.arm()
time.sleep(2)

print("Taking Off!")
my_pluto.take_off()
time.sleep(3) # Hover for 3 seconds

print("Landing...")
my_pluto.land()
time.sleep(2)

my_pluto.disarm()
my_pluto.disconnect()
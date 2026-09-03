from plutocontrol import Pluto
import threading
import keyboard

pluto = Pluto()
pluto.connect()
pluto.arm()


def control_loop():
    while True:
        if keyboard.is_pressed("w"):
            pluto.forward()
        elif keyboard.is_pressed("s"):
            pluto.backward()
        elif keyboard.is_pressed("a"):
            pluto.left()
        elif keyboard.is_pressed("d"):
            pluto.right()
        elif keyboard.is_pressed("space"):
            pluto.take_off()
        elif keyboard.is_pressed("x"):
            pluto.land()
        elif keyboard.is_pressed("q"):
            break  # Quit
        else:
            # Reset RC to neutral if keys released
            pluto.rcPitch = 1500
            pluto.rcRoll = 1500


control_loop()
pluto.disarm()
pluto.disconnect()

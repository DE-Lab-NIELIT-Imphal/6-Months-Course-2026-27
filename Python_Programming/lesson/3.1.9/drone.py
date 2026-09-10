try:
    altitude = float(input("Enter altitude: "))
    battery = int(input("Enter battery: "))

    with open("drone_log.txt", "a") as file:
        file.write(f"Altitude: {altitude} m, Battery: {battery}%\n")

    print("Log saved successfully.")

except ValueError:
    print("Error: Enter valid numeric values.")

except IOError:
    print("Error: Could not write to drone log file.")

finally:
    print("Logging operation completed.")

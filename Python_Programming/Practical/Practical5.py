import serial
import time

# UART_PORT = '/dev/ttyAMA0'
UART_PORT = "/dev/ttyS0"
BAUD_RATE = 115200
THRESHOLD = 100  # cm - closer than this triggers an alert

# -- Open serial port ------------------------------------------------------
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)
time.sleep(0.1)


# -- TFMini-S frame parser -------------------------------------------------
def read_distance():
    while True:
        if ser.read(1) == b"\x59":
            if ser.read(1) == b"\x59":
                frame = ser.read(7)
                dist = frame[0] + (frame[1] << 8)
                return dist


# -- Classification using if-elif-else -------------------------------------
def classify(distance):
    if distance < 30:
        return "CRITICAL"
    elif distance < 100:
        return "WARNING"
    else:
        return "CLEAR"


# -- for loop: 10 samples with running average -----------------------------
print("-- Sampling 10 readings --")
total = 0
for i in range(1, 11):
    dist = read_distance()
    total += dist
    running_avg = total / i
    band = classify(dist)
    print(f"Sample {i:2d}: {dist:4d} cm | avg = {running_avg:6.1f} cm | band = {band}")
    time.sleep(0.1)

# -- while True: continuous monitor with threshold alert -------------------
print("\n-- Continuous monitor (Ctrl+C to stop) --")
try:
    while True:
        dist = read_distance()
        band = classify(dist)
        if dist < THRESHOLD:
            print(f"[ALERT] Obstacle at {dist} cm (< {THRESHOLD} cm) - band: {band}")
        else:
            print(f"Distance: {dist} cm - {band}")
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
    ser.close()

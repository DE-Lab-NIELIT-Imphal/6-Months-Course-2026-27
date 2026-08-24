import board
import adafruit_dht
import RPi.GPIO as GPIO

# DHT22 DATA connected to GPIO17
dht = adafruit_dht.DHT22(board.D17)
# DHT11 DATA connected to GPIO17
dht = adafruit_dht.DHT11(board.D17)

trigger_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.IN)

temperature = dht.temperature
humidity = dht.humidity

threshold_exceeded = temperature > 30.0

print("\n--- DHT22 SENSOR DATA ---")

print(f"temperature          value={temperature}    type={type(temperature).__name__}")
print(f"humidity             value={humidity}    type={type(humidity).__name__}")
print(
    f"trigger_pin          value={trigger_pin}         type={type(trigger_pin).__name__}"
)
print(
    f"threshold_exceeded   value={threshold_exceeded}      type={type(threshold_exceeded).__name__}"
)

digital_state = bool(GPIO.input(trigger_pin))

print("\n--- DIGITAL GPIO ---")

print(f"digital_state={digital_state} " f"({type(digital_state).__name__})")

expected_types = {"temp": float, "humidity": float, "motion": bool, "pin": int}

sample_reading = {
    "temp": temperature,
    "humidity": humidity,
    "motion": digital_state,
    "pin": trigger_pin,
}

print("\n--- TYPE VALIDATION ---")

for key, value in sample_reading.items():

    if isinstance(value, expected_types[key]):
        status = "OK"
    else:
        status = "TYPE MISMATCH"

    print(f"{key:<10} -> {status}")

GPIO.cleanup()
dht.exit()

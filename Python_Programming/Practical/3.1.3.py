import board
import adafruit_dht

# DHT22 DATA connected to GPIO17
dht = adafruit_dht.DHT22(board.D17)
# DHT11 DATA connected to GPIO17
dht = adafruit_dht.DHT11(board.D17)

# ── Safe operating ranges ──────────────────────────────────────────────────
TEMP_MIN, TEMP_MAX = 15.0, 35.0  # °C
HUMIDITY_MIN, HUMIDITY_MAX = 20.0, 70.0  # %
HEAT_IDX_MIN, HEAT_IDX_MAX = 15.0, 38.0  # °C (feels-like safe band)

# ── 1. Read live sensor data ───────────────────────────────────────────────
temp_c = dht.temperature
humidity = dht.humidity

# ── 2. Arithmetic: unit conversion ────────────────────────────────────────
temp_f = (temp_c * 9 / 5) + 32
print(f"Temperature : {temp_c:.1f} °C  /  {temp_f:.1f} °F")
print(f"Humidity    : {humidity:.1f} %")

# ── 3. Arithmetic: Steadman Heat Index formula ────────────────────────────
T, H = temp_c, humidity
heat_index = (
    -8.78469475556
    + 1.61139411 * T
    + 2.33854883889 * H
    - 0.14611605 * T * H
    - 0.012308094 * T**2
    - 0.016424828 * H**2
    + 0.002211732 * T**2 * H
    + 0.00072546 * T * H**2
    - 0.000003582 * T**2 * H**2
)
print(f"Heat Index  : {heat_index:.1f} °C (feels-like)")

# ── 4. Comparison operators: individual safe-range checks ─────────────────
is_temp_safe = TEMP_MIN <= temp_c <= TEMP_MAX
is_humidity_safe = HUMIDITY_MIN <= humidity <= HUMIDITY_MAX
is_heatindex_safe = HEAT_IDX_MIN <= heat_index <= HEAT_IDX_MAX

print(f"\nTemp safe?        {is_temp_safe}   ({TEMP_MIN}-{TEMP_MAX} °C)")
print(f"Humidity safe?    {is_humidity_safe}   ({HUMIDITY_MIN}-{HUMIDITY_MAX} %)")
print(f"Heat index safe?  {is_heatindex_safe}   ({HEAT_IDX_MIN}-{HEAT_IDX_MAX} °C)")

# ── 5. Logical operators: compound pre-flight verdict ─────────────────────
overall_safe = is_temp_safe and is_humidity_safe and is_heatindex_safe
verdict = "SAFE TO FLY" if overall_safe else "DO NOT FLY"

print(f"\nPre-flight verdict: {verdict}")

if not is_temp_safe:
    print(f"  ✗ Temperature {temp_c:.1f} °C is outside safe range")
if not is_humidity_safe:
    print(f"  ✗ Humidity {humidity:.1f} % is outside safe range")
if not is_heatindex_safe:
    print(f"  ✗ Heat index {heat_index:.1f} °C is outside safe range")

dht.exit()

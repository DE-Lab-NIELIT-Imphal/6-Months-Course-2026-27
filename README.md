# Drone AI Systems & Security Associate

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Course](https://img.shields.io/badge/Course-Drone%20AI%20%26%20Security%20Associate-green.svg)
![Lab](https://img.shields.io/badge/Lab-Drone%20Electronics%20Lab-orange.svg)
![Institution](https://img.shields.io/badge/Institution-NIELIT%20Imphal-red.svg)

This repository contains the tracked practical code, hardware interfacing experiments, and core lesson scripts for the **Drone AI Systems & Security Associate (6 Months Course, 2026–2027)** conducted at **Drone Electronics Lab (DE-Lab), NIELIT Imphal**.

---

> [!NOTE]
> **Educational & Laboratory Purpose Only**  
> All source code, telemetry algorithms, flight safety logic, and hardware sensor routines in this repository are strictly developed for academic, educational, and laboratory training purposes.

---

## 📖 Course Curriculum Overview

The 6-month curriculum spans six specialized domains in unmanned aerial vehicle (UAV) engineering, flight electronics, and security:

1. **Drone Fundamentals**: UAV airframe classifications, aerodynamics, multirotor dynamics, ESCs, motors, and flight controller architecture.
2. **Drone Applications**: Precision agriculture, surveying, delivery systems, infrastructure inspection, and operational safety.
3. **Python Programming for Drones (Current Focus)**: Python syntax, data structures, control logic, modular programming, telemetry math, hardware sensor interfacing (Raspberry Pi GPIO, DHT sensors), string parsing, and flight logging.
4. **AI / ML for Drones**: Computer vision, edge object detection (YOLO/SSD), aerial imagery processing, and autonomous navigation models.
5. **Drone Communications**: RF spectrum fundamentals, MAVLink telemetry protocol, transmitter/receiver binding, and telemetry radio link analysis.
6. **Drone Security**: Threat modeling, GPS/telemetry anti-spoofing, RF jamming detection, secure communication links, and cyber-physical security audits.

---

## 🗂 Repository Structure

```text
.
├── Python_Programming/
│   ├── Practical/                                # Hardware & sensor interfacing practicals
│   │   ├── 3.1.2.py                              # DHT11/DHT22 & GPIO sensor data extraction and type validation
│   │   └── 3.1.3.py                              # Environmental safety checks & Steadman Heat Index calculation
│   └── lesson/                                   # Core concept lessons and algorithmic modules
│       ├── 3.1.2.py                              # Variables, data types, and telemetry data structures
│       ├── 3.1.3.py                              # Operators, hover endurance math, and arming logic
│       ├── 3.1.4.py                              # Selection structures and waypoint / GPS locking loops
│       ├── 3.1.4_2.py                            # Loop controls (break failsafes, continue no-fly, pass stubs)
│       ├── 3.1.5.py                              # Basic function declaration demo
│       ├── 3.1.5/                                # Modular preflight & mission execution system
│       │   ├── battery.py                        # 4S pack voltage percentage and status evaluation
│       │   ├── preflight.py                      # Multi-subsystem health diagnostics engine
│       │   ├── mission.py                        # Flat-earth waypoint distance calculation and navigation
│       │   ├── param_arg.py                      # Parameter types (positional, default, keyword, *args, **kwargs)
│       │   └── main.py                           # Master flight execution pipeline
│       ├── 3.1.6/                                # Python collections & pre-flight arming assignment
│       │   ├── list_demo.py                      # Altitude log array manipulation and methods
│       │   ├── dict_demo.py                      # Dynamic vehicle state telemetry dictionary methods
│       │   ├── tuple_demo.py                     # Waypoint tuples, unpacking, and namedtuple definitions
│       │   └── assignment/                       # Modular pre-flight arming validation assignment
│       │       ├── check.py                      # Diagnostic rule evaluation (GPS fix, satellites, battery)
│       │       └── main.py                       # Formatted test harness runner
│       ├── 3.1.7.py                              # String formatting, telemetry stream parsing, and byte encoding
│       ├── 3.1.7-lesson.py                       # String methods practice and telemetry manipulation
│       └── 3.1.8/                                # File handling & flight data telemetry logging
│           ├── code.py                           # File I/O modes (read, write, append, context manager)
│           ├── data.txt                          # Flight mode sample text file
│           └── implementation/                   # Flight telemetry CSV logging pipeline
│               ├── code.py                       # Telemetry serialization via csv.DictWriter
│               └── log.csv                       # Generated 10-DOF telemetry CSV log
├── .gitignore                                    # Git ignore patterns (bytecode, virtual environments, zips)
├── LICENSE                                       # MIT License
└── README.md                                     # Course & repository documentation
```

---

## 🔬 Module Breakdown & Code Analysis

### 1. Hardware Interfacing & Sensor Practicals (`Python_Programming/Practical/`)

* **[`Practical/3.1.2.py`](file:///R:/Code/NIELIT/Python_Programming/Practical/3.1.2.py)**:
  * Interfacing Raspberry Pi GPIO with Adafruit DHT11 / DHT22 environmental sensors and digital motion triggers.
  * Demonstrates sensor value extraction (`temperature`, `humidity`), threshold validation, and programmatic type-checking against a predefined schema dictionary.
* **[`Practical/3.1.3.py`](file:///R:/Code/NIELIT/Python_Programming/Practical/3.1.3.py)**:
  * Implements multi-variable environmental safety gating for UAV operations.
  * Calculates Celsius-to-Fahrenheit conversion and the empirical **Steadman Heat Index** (feels-like temperature).
  * Evaluates chained comparison and logical operators to yield a deterministic pre-flight verdict (`SAFE TO FLY` vs. `DO NOT FLY`).

### 2. Python Fundamentals & Control Structures (`Python_Programming/lesson/3.1.2 - 3.1.4`)

* **[`lesson/3.1.2.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.2.py)**: Demonstrates fundamental data primitives (strings, floats, booleans, integers) and complex structures (tuples for GPS coordinates, lists for payload types, dictionaries for IMU/GPS/barometer status).
* **[`lesson/3.1.3.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.3.py)**: Telemetry math including hover time calculation (`(capacity / 1000) / current_draw`), per-cell voltage cutoff validation, logical arming prerequisites, and modulo waypoint checkpoint detection.
* **[`lesson/3.1.4.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.4.py)**: Decision trees for autonomous mode transitions (RTL on low battery, HOLD on wind gusts, DESCEND on ceiling breach) alongside `for` loops iterating waypoints and `while` loops simulating satellite lock acquisition.
* **[`lesson/3.1.4_2.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.4_2.py)**: Loop control mechanisms in flight systems:
  * `break`: Immediate failsafe motor cutoff upon critical IMU faults.
  * `continue`: Dynamic skipping of no-fly / geofence restricted waypoints.
  * `pass`: Flight controller mode handler stubs (LOITER, GUIDED, LAND).

### 3. Modular Programming & UAV Flight Engine (`Python_Programming/lesson/3.1.5/`)

* **[`lesson/3.1.5/battery.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.5/battery.py)**: Battery percentage estimation (`get_battery_percentage`) for 4S LiPo configurations (14.0V–16.8V) and health classification (`GOOD`, `LOW`, `CRITICAL`).
* **[`lesson/3.1.5/preflight.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.5/preflight.py)**: Master diagnostic function `run_preflight()` aggregating battery state, satellite lock thresholds (min 6 sats), and sensor health maps.
* **[`lesson/3.1.5/mission.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.5/mission.py)**: Flat-earth Euclidean coordinate distance calculator (`calc_distance`) and autonomous mission simulator (`run_mission`) with restricted zone avoidance.
* **[`lesson/3.1.5/param_arg.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.5/param_arg.py)**: Demonstration of positional parameters, default arguments, keyword arguments, arbitrary arguments (`*args` for waypoint tuples), and keyword telemetry dictionaries (`**kwargs`).
* **[`lesson/3.1.5/main.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.5/main.py)**: Integrated entry point running automated preflight diagnostic gating before launching simulated autonomous flight missions.

### 4. Data Collections & Pre-Flight Diagnostics (`Python_Programming/lesson/3.1.6/`)

* **[`lesson/3.1.6/list_demo.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/list_demo.py)**: In-depth operations on altitude logs (`append`, `insert`, `extend`, `remove`, `pop`, `index`, `sort`, `reverse`, `copy`, `clear`).
* **[`lesson/3.1.6/dict_demo.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/dict_demo.py)**: Telemetry dictionary inspection, key manipulation, safe lookup (`get`), default values (`setdefault`), batch updates (`update`), and cleanups (`popitem`, `clear`).
* **[`lesson/3.1.6/tuple_demo.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/tuple_demo.py)**: Coordinate immutability, tuple unpacking (`lat, lon, alt = home`), and structured data representation via `collections.namedtuple`.
* **[`lesson/3.1.6/assignment/`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/assignment/)**:
  * **[`check.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/assignment/check.py)**: Core validation engine verifying GPS fix (minimum 3D fix), satellite count (minimum 8), loaded waypoints (> 0), and battery voltage (>= 14.8V).
  * **[`main.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.6/assignment/main.py)**: Test runner executing diagnostic reports across multiple UAV profiles (`UAV-01`, `UAV-02`).

### 5. String Processing & Telemetry Serialization (`Python_Programming/lesson/3.1.7.py`)

* **[`lesson/3.1.7.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.7.py)**:
  * String interpolation with f-string precision (`{altitude:.2f}`) and alignment padding (`{field:<12}`).
  * Parsing comma-separated telemetry streams with `split()` and rebuilding CSV records with `join()`.
  * Sanitizing noisy serial streams with `strip()`, transforming MAVLink flight modes (`upper()`, `replace()`), filename formatting (`zfill()`), and UTF-8 encoding/decoding (`encode()`, `decode()`) for network socket and MAVLink transmission.

### 6. Flight Data Logging & File I/O (`Python_Programming/lesson/3.1.8/`)

* **[`lesson/3.1.8/code.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.8/code.py)**: Standard file operations (`read`, `write`, `append`) and safe context management (`with open()`).
* **[`lesson/3.1.8/implementation/code.py`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.8/implementation/code.py)**: Structured 10-DOF telemetry logging pipeline serializing flight status dictionaries (timestamp, coordinates, altitude, speed, attitude roll/pitch/yaw, battery %, satellites) into CSV format using `csv.DictWriter`.
* **[`lesson/3.1.8/implementation/log.csv`](file:///R:/Code/NIELIT/Python_Programming/lesson/3.1.8/implementation/log.csv)**: Output log generated by the flight telemetry serialization script.

---

## 🚀 Student Quickstart & Execution Guide

### 1. Prerequisites

- Python 3.8 or higher installed.
- Git for version control.
- *(Optional for Hardware Practicals)*: Raspberry Pi with `RPi.GPIO` and `adafruit-circuitpython-dht` installed.

### 2. Environment Setup

Clone the repository and set up a local virtual environment:

```bash
git clone https://github.com/NIELIT-Imphal/Drone-AI-Security-Associate.git
cd Drone-AI-Security-Associate
python -m venv ./nielit_env
```

Activate the virtual environment:

* **Windows (PowerShell):**
  ```powershell
  .\nielit_env\Scripts\Activate.ps1
  ```
* **Linux / macOS:**
  ```bash
  source ./nielit_env/bin/activate
  ```

*(Optional - For Raspberry Pi Sensor Practicals)*:
```bash
pip install RPi.GPIO adafruit-circuitpython-dht
```

### 3. Running Lesson Scripts & Practicals

Execute scripts from the repository root:

#### A. Core Lessons (Syntax, Logic, Collections, Strings, Files)
```bash
# Variables & Data Types
python ./Python_Programming/lesson/3.1.2.py

# Operators & Telemetry Calculations
python ./Python_Programming/lesson/3.1.3.py

# Control Flow & Loops
python ./Python_Programming/lesson/3.1.4.py
python ./Python_Programming/lesson/3.1.4_2.py

# Data Structures (Lists, Dicts, Tuples)
python ./Python_Programming/lesson/3.1.6/list_demo.py
python ./Python_Programming/lesson/3.1.6/dict_demo.py
python ./Python_Programming/lesson/3.1.6/tuple_demo.py

# String Processing & Telemetry Parsing
python ./Python_Programming/lesson/3.1.7.py

# File Handling & CSV Flight Telemetry Logging
python ./Python_Programming/lesson/3.1.8/code.py
python ./Python_Programming/lesson/3.1.8/implementation/code.py
```

#### B. Modular Pre-Flight & Navigation System
```bash
# Run modular pre-flight and waypoint mission
python ./Python_Programming/lesson/3.1.5/main.py

# Run function parameter and argument demonstrations
python ./Python_Programming/lesson/3.1.5/param_arg.py
```

#### C. Pre-Flight Diagnostics Assignment Test Harness
```bash
# Run arming diagnostic validation test cases
python ./Python_Programming/lesson/3.1.6/assignment/main.py
```

#### D. Hardware Sensor Practicals (Run on Raspberry Pi hardware)
```bash
# DHT Sensor & GPIO validation
python ./Python_Programming/Practical/3.1.2.py

# Environmental safety checks & Steadman Heat Index
python ./Python_Programming/Practical/3.1.3.py
```

---

## 🛡️ Laboratory Safety & Operational Guidelines

- **Pre-Arming Verification**: Always ensure pre-flight diagnostics pass before arming motors in laboratory or field settings.
- **Geofence Enforcement**: Verify waypoints against no-fly zones and restricted airspace before uploading mission plans.
- **Hardware Circuit Safety**: Always power down the Raspberry Pi / development board before connecting or modifying GPIO sensor wiring.
- **RF & Spectrum Compliance**: Ensure all telemetry radio and RC links operate within local regulatory frequency allocations (e.g., 2.4 GHz, 433 MHz, 868/915 MHz).

---

## 📜 License & Attribution

This project is licensed under the **MIT License**.

Copyright (c) 2026 **Drone Electronics Lab, NIELIT Imphal**

Refer to the [`LICENSE`](file:///R:/Code/NIELIT/LICENSE) file for complete terms.


# Drone AI Systems & Security Associate

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Course](https://img.shields.io/badge/Course-Drone%20AI%20%26%20Security%20Associate-green.svg)
![Lab](https://img.shields.io/badge/Lab-Drone%20Electronics%20Lab-orange.svg)
![Institution](https://img.shields.io/badge/Institution-NIELIT%20Imphal-red.svg)

This repository contains the tracked practical code and lesson scripts for the **Drone AI Systems & Security Associate (6 Months Course)** conducted at **Drone Electronics Lab, NIELIT Imphal**.

---

> *NOTE*
> **Educational Purpose Only**  
> All source code, telemetry routines, and lesson exercises in this repository are strictly developed for academic, educational, and laboratory training purposes.

---

## Program Modules

The course curriculum is structured across six core areas:

1. **Drone Fundamentals**: Aerodynamics, UAV hardware components, and flight mechanics.
2. **Drone Applications**: Real-world industrial usage and operational frameworks.
3. **Python Programming for Drones**: Fundamentals of Python syntax, data structures, control flow, and telemetry calculations.
4. **AI / ML for Drones**: Computer vision, object detection, and autonomous edge processing.
5. **Drone Communications**: RF spectrum fundamentals, MAVLink protocol, and telemetry links.
6. **Drone Security**: Cybersecurity fundamentals, telemetry security, and anti-spoofing techniques.

---

## Repository Structure

```text
.
├── AI_Ml_Drones/           # Modules for AI/ML and computer vision algorithms
├── Drone_Communications/   # Telemetry and communications laboratory code
├── Drone_Fundamentals/     # Hardware and flight dynamics modules
├── Drone_Security/         # Cyber security and RF safety analysis
├── Python_Programming/     # Python lessons and core scripts
│   └── lesson/             # Structured lesson code
│       ├── 3.1.2.py        # Data types and drone status structures
│       ├── 3.1.3.py        # Telemetry calculations and expressions
│       ├── 3.1.4.py        # Selection and iteration control flow
│       └── 3.1.4_2.py      # Loop control (break, continue, pass)
├── .gitignore              # Ignored local lab configurations and outputs
├── LICENSE                 # MIT License file
└── README.md               # Course documentation
```

---

## Student Quickstart & Execution Guide

### 1. Prerequisites

- Python 3.8 or higher installed on your local environment.
- Git for repository cloning and version control.

### 2. Environment Setup

Clone the repository and set up a local Python virtual environment using relative paths:

```bash
git clone https://github.com/NIELIT-Imphal/Drone-AI-Security-Associate.git
cd Drone-AI-Security-Associate
python -m venv ./nielit_env
```

Activate the virtual environment:

- **Windows (PowerShell):**
  ```powershell
  .\nielit_env\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  source ./nielit_env/bin/activate
  ```

### 3. Running Lesson Scripts

To execute tracked Python lesson scripts, run them from the repository root:

```bash
python ./Python_Programming/lesson/3.1.2.py
python ./Python_Programming/lesson/3.1.3.py
python ./Python_Programming/lesson/3.1.4.py
python ./Python_Programming/lesson/3.1.4_2.py
```

---

## Laboratory Safety & Operational Guidelines

- **Educational Environment**: All code must be reviewed and executed under instructor supervision.
- **Spectrum Compliance**: RF and telemetry experiments must comply with local frequency and spectrum regulations.

---

## License

This project is licensed under the **MIT License**.

Copyright (c) 2026 **Drone Electronics Lab, NIELIT Imphal**

Refer to the [`LICENSE`](LICENSE) file for complete licensing terms.

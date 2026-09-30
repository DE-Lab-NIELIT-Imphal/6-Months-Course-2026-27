# YOLO Object Detection with Real-Time FPS

Object detection implementation using Ultralytics YOLO with real-time FPS overlay, supporting webcam streams, video files, and static images.

---

## Directory Structure

```text
object_detection/
│
├── models/             # Downloaded or custom trained YOLO weights (*.pt)
├── images/             # Input test images
├── videos/             # Input test videos
├── results/            # Detection outputs with FPS overlay
├── resource/           # Reference images and screenshots
├── Reference.pdf       # Course reference documentation
├── detect.py           # Full-featured detection script (CLI options, GPU/CPU, save)
├── simple_detect.py    # Minimal script for webcam detection on CPU with FPS (no save)
└── Readme.md           # Project documentation
```

---

## Quick Start (Minimal CPU Webcam Detection)

To launch straightforward webcam detection on CPU with zero file saving and live FPS:

```powershell
python simple_detect.py
```
*Press `q`, `x`, or `ESC` to quit.*

---

## Advanced Usage (`detect.py`)

### 1. Webcam Stream (Default)
```powershell
python detect.py
```
Or specify webcam index and device explicitly:
```powershell
python detect.py --source 0 --device cuda
```

### 2. Static Image Detection
```powershell
python detect.py --source images/test.jpg --device cuda
```

### 3. Video File Detection
```powershell
python detect.py --source videos/video.mp4 --device cuda --save
```

### 4. Filter Specific Object Classes
Detect only people (`0`) or people and cars (`0 2`):
```powershell
python detect.py --classes 0 2 --conf 0.5
```

---

## Command Line Arguments

| Argument | Default | Description |
|---|---|---|
| `--model` | `yolo11n.pt` | Path or name of YOLO model |
| `--source` | `0` | Webcam index (`0`), image path, or video path |
| `--classes` | `None` | Class IDs to detect (e.g. `--classes 0 2`) |
| `--device` | `auto` | Inference device (`auto`, `cuda`, `cpu`, `0`) |
| `--conf` | `0.5` | Minimum confidence score threshold |
| `--show` / `--no-show` | `True` | Display live OpenCV detection window |
| `--save` / `--no-save` | `True` | Save annotated output with FPS badge to `results/` |

---

## Real-Time FPS Overlay

The script continuously measures:
- **Streaming FPS:** Exponential moving average ($1.0 / \Delta t$) for smooth, non-flickering frame-rate display.
- **Inference Latency:** Preprocess + Inference + Postprocess time in milliseconds (`result.speed`).
- **High-Contrast Badge:** Rendered in the top-left corner with a dark border box so it remains visible against any video background.

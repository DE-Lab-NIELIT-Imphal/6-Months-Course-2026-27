"""Simple YOLO Webcam Object Detection on CPU with FPS Overlay.

Runs real-time inference on CPU without saving results to disk.
"""

import time
import cv2
import numpy as np
from ultralytics import YOLO


def draw_fps(frame: np.ndarray, fps: float) -> None:
    """Draw a high-visibility FPS counter on the frame."""
    text: str = f"FPS: {fps:.1f}"
    # Contrast outline for clear visibility against any background
    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 0, 0),
        4,
        cv2.LINE_AA,
    )


def run_webcam_detection() -> None:
    """Run real-time YOLO detection from webcam on CPU."""
    model = YOLO("yolo11n.pt")
    prev_time: float = time.perf_counter()

    print("Starting webcam detection on CPU...")
    print("Press 'q', 'x', or 'ESC' to exit.")

    results = model.predict(source=1, device="cpu", stream=True)

    for result in results:
        frame: np.ndarray = result.plot()

        curr_time: float = time.perf_counter()
        dt: float = curr_time - prev_time
        prev_time = curr_time
        fps: float = 1.0 / dt if dt > 0 else 0.0

        draw_fps(frame, fps)

        cv2.imshow("YOLO Webcam Detection (CPU)", frame)
        key: int = cv2.waitKey(1) & 0xFF
        if key in (ord("q"), ord("x"), 27):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_webcam_detection()

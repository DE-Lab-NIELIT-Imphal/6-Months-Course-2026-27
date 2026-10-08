"""YOLO Object Detection with real-time FPS overlay.

Supports webcam, video, and image inference using Ultralytics YOLO.
"""

import argparse
from pathlib import Path
import time
import cv2
import numpy as np
import torch
from ultralytics import YOLO


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for YOLO detection."""
    p = argparse.ArgumentParser(description="YOLO Object Detection")
    p.add_argument("--model", default="yolo11n.pt", help="Path to YOLO model")
    p.add_argument(
        "--source", default="0", help="Image, video, or webcam source"
    )
    p.add_argument(
        "--classes", nargs="+", type=int, default=None, help="Class IDs"
    )
    p.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cpu", "cuda", "0"],
        help="Inference device",
    )
    p.add_argument("--conf", type=float, default=0.5, help="Confidence")
    p.add_argument(
        "--show",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Display live window (--show / --no-show)",
    )
    p.add_argument(
        "--save",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Save output results (--save / --no-save)",
    )
    return p.parse_args()


def resolve_device(requested_device: str) -> str:
    """Determine inference device based on user input and CUDA status."""
    if requested_device == "auto":
        return "cuda:0" if torch.cuda.is_available() else "cpu"
    if requested_device == "cuda":
        return "cuda:0"
    return requested_device


def draw_fps_badge(
    frame: np.ndarray, fps: float, latency_ms: float = 0.0
) -> np.ndarray:
    """Draw a high-contrast FPS and latency badge on top-left of frame."""
    badge_text: str = f"FPS: {fps:.1f}"
    if latency_ms > 0:
        badge_text += f" ({latency_ms:.1f}ms)"

    (w, h), _ = cv2.getTextSize(badge_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
    cv2.rectangle(frame, (10, 10), (22 + w, 22 + h + 8), (0, 0, 0), -1)
    cv2.rectangle(frame, (10, 10), (22 + w, 22 + h + 8), (0, 255, 0), 2)
    cv2.putText(
        frame,
        badge_text,
        (16, 16 + h),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )
    return frame


def is_image_source(source_val: int | str) -> bool:
    """Check if the provided source represents a static image file."""
    if isinstance(source_val, int):
        return False
    image_exts: tuple[str, ...] = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp",
        ".tiff",
    )
    return Path(str(source_val)).suffix.lower() in image_exts


def print_banner(args: argparse.Namespace, device: str) -> None:
    """Display runtime configuration banner."""
    print("=" * 50)
    print("YOLO OBJECT DETECTION WITH REAL-TIME FPS")
    print("=" * 50)
    print(f"Model   : {args.model}")
    print(f"Source  : {args.source}")
    print(f"Device  : {device}")
    print(f"Classes : {args.classes}")
    print(f"Conf.   : {args.conf}")
    if device.startswith("cuda"):
        print(f"GPU     : {torch.cuda.get_device_name(0)}")
    print("=" * 50)
    print("Press 'q', 'x', or 'ESC' to exit display window.\n")


def create_video_writer(
    save_path: Path, frame: np.ndarray, fps: float = 30.0
) -> cv2.VideoWriter:
    """Initialize an OpenCV VideoWriter for saving output stream."""
    h, w = frame.shape[:2]
    fourcc: int = cv2.VideoWriter_fourcc(*"mp4v")
    return cv2.VideoWriter(str(save_path), fourcc, fps, (w, h))


def update_fps(
    prev_time: float, fps_smooth: float, alpha: float = 0.15
) -> tuple[float, float]:
    """Calculate exponentially smoothed real-time FPS."""
    curr_time: float = time.perf_counter()
    dt: float = curr_time - prev_time
    inst_fps: float = 1.0 / dt if dt > 0 else 0.0
    smooth: float = (
        inst_fps
        if fps_smooth == 0.0
        else alpha * inst_fps + (1.0 - alpha) * fps_smooth
    )
    return curr_time, smooth


def handle_save_output(
    frame: np.ndarray,
    is_img: bool,
    source: int | str,
    writer: cv2.VideoWriter | None,
    results_dir: Path,
) -> cv2.VideoWriter | None:
    """Save detected image or append frame to video writer."""
    if is_img:
        out_file: Path = results_dir / f"result_{Path(str(source)).name}"
        cv2.imwrite(str(out_file), frame)
        print(f"Saved detected image to {out_file}")
        return None
    if writer is None:
        writer = create_video_writer(results_dir / "output.mp4", frame, 30.0)
    writer.write(frame)
    return writer


def handle_display_window(frame: np.ndarray, is_img: bool, show: bool) -> bool:
    """Display frame in window and return True if exit key was pressed."""
    if not show:
        return False
    try:
        cv2.imshow("YOLO Object Detection", frame)
        key: int = cv2.waitKey(0 if is_img else 1) & 0xFF
        return key in (ord("q"), ord("x"), 27)
    except cv2.error:
        return False


def process_detections(
    model: YOLO,
    source: int | str,
    device: str,
    args: argparse.Namespace,
) -> None:
    """Stream inference from source, compute FPS, and display/save."""
    is_img: bool = is_image_source(source)
    results_dir: Path = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    writer: cv2.VideoWriter | None = None

    prev_time: float = time.perf_counter()
    fps_smooth: float = 0.0

    results = model.predict(
        source=source,
        device=device,
        classes=args.classes,
        conf=args.conf,
        stream=True,
    )

    for result in results:
        frame: np.ndarray = result.plot()
        prev_time, fps_smooth = update_fps(prev_time, fps_smooth)
        latency_ms: float = float(sum(result.speed.values()))

        draw_fps_badge(frame, fps_smooth, latency_ms)

        if args.save:
            writer = handle_save_output(
                frame, is_img, source, writer, results_dir
            )

        if handle_display_window(frame, is_img, args.show):
            break

    if writer is not None:
        writer.release()
        print(f"Saved output video to {results_dir / 'output.mp4'}")
    cv2.destroyAllWindows()


def main() -> None:
    """Main execution entry point."""
    args = parse_arguments()
    device: str = resolve_device(args.device)
    print_banner(args, device)

    model = YOLO(args.model)
    source: int | str = (
        int(args.source) if str(args.source).isdigit() else args.source
    )

    process_detections(model, source, device, args)
    print("\nDetection completed successfully.")


if __name__ == "__main__":
    main()

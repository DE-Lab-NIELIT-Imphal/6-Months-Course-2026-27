import os
import socket
import time
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Generator
import urllib.request

import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

weights_file = "yolo11n.pt" if os.path.exists("yolo11n.pt") else "yolov5n.pt"
model = YOLO(weights_file)
camera_index = int(os.getenv("CAMERA_INDEX", "0"))
cap = cv2.VideoCapture(camera_index)


def get_local_ip() -> str:
    """Retrieve host local network IP address."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return str(sock.getsockname()[0])
    except Exception:
        return "127.0.0.1"
    finally:
        sock.close()


def get_public_ip() -> str | None:
    """Retrieve external public IP address if reachable."""
    try:
        url = "https://api.ipify.org"
        with urllib.request.urlopen(url, timeout=1.5) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception:
        return None


def get_detection_frame() -> Generator[bytes, None, None]:
    """Capture webcam frame, compute FPS, run YOLO detection, and yield stream."""
    prev_time = time.time()
    fps = 0.0

    while cap.isOpened():
        success, frame = cap.read()
        if not success or frame is None:
            continue

        curr_time = time.time()
        dt = curr_time - prev_time
        prev_time = curr_time
        if dt > 0:
            fps = 0.9 * fps + 0.1 * (1.0 / dt) if fps > 0 else (1.0 / dt)

        results = model.predict(frame, classes=[0], conf=0.5, verbose=False)
        annotated_frame = results[0].plot()

        cv2.putText(
            annotated_frame,
            f"FPS: {fps:.1f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        ok, buffer = cv2.imencode(".jpg", annotated_frame)
        if ok:
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
            )


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Release camera resource on server shutdown."""
    yield
    if cap.isOpened():
        cap.release()


app = FastAPI(title="Webcam Person Detection", lifespan=lifespan)


@app.get("/")
@app.get("/stream")
def stream_detections() -> StreamingResponse:
    """Stream live webcam detection frames over HTTP."""
    return StreamingResponse(
        get_detection_frame(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    print("\n" + "=" * 55)
    print("🎥  STREAM SERVER READY")
    print("=" * 55)
    print(f"💻 Localhost (This PC)       : http://localhost:{port}/")
    print(f"📱 Local Network (Same Wi-Fi): http://{local_ip}:{port}/")
    if public_ip:
        print(f"🌐 Public IP (Internet)      : http://{public_ip}:{port}/")
    print("=" * 55)
    print("💡 To view over the internet without router port forwarding:")
    print(f"   Run in another terminal: npx localtunnel --port {port}\n")

    uvicorn.run(app, host=host, port=port)

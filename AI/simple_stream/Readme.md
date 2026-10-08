# YOLO Live Stream over Local Network & Internet

A FastAPI application that streams real-time YOLO object detection (person detection) from a webcam over HTTP (MJPEG). It is configured to bind to `0.0.0.0`, enabling access from any smartphone, tablet, or PC on the same Wi-Fi network as well as over the internet.

---

## Features

- **Local Network Access (Wi-Fi / LAN):** Binds to `0.0.0.0` so any device connected to the same Wi-Fi can view the stream.
- **Internet Access:** Supports direct access via public IP (port forwarding) or instant zero-config tunnels (`localtunnel`, `cloudflared`, `ngrok`).
- **Thread-Safe Multi-Client Streaming:** Dedicated background thread processes camera frames once and broadcasts to multiple connected devices simultaneously without frame dropping or camera lock contention.
- **Live FPS Counter:** Measures frame delta time and overlays high-contrast green-and-black FPS text on the video.
- **Web UI & API Endpoints:** Responsive mobile-first HTML viewer on `/` and raw MJPEG stream on `/stream`.

---

## Quick Start

### 1. Run the Server
```powershell
python main.py
```

### 2. Access the Stream

On startup, the console displays all active connection URLs:

```text
==============================================================
🎥  YOLO LIVE STREAM SERVER RUNNING
==============================================================
💻 Localhost (This PC)       : http://localhost:8080/
📱 Local Network (Same Wi-Fi): http://192.168.1.119:8080/
🌐 Public IP (Port Forward)  : http://14.139.207.244:8080/
==============================================================
```

#### A. From the Same Computer:
Open: `http://localhost:8080/`

#### B. From Your Phone or Any Device on the Same Wi-Fi:
Open your phone's browser and type the **Local Network** URL:
```text
http://<your_local_ip>:8080/  (e.g., http://192.168.1.119:8080/)
```

#### C. Access Over the Internet (From Anywhere in the World):
To share your stream with anyone on mobile data (4G/5G) or outside your local Wi-Fi without configuring router port forwarding:

Open a new terminal and run:
```powershell
npx localtunnel --port 8080
```
This gives you an instant public HTTPS link (e.g., `https://random-name.loca.lt`) accessible worldwide.

---

## API Endpoints

| Endpoint | Method | Response | Description |
|---|---|---|---|
| `/` | `GET` | HTML | Responsive HTML5 video stream viewer |
| `/stream` | `GET` | `multipart/x-mixed-replace` | Pure MJPEG video stream (for `<img src>` or VLC) |
| `/status` | `GET` | JSON | Server status, current FPS, model, and local IP |

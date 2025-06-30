# test_yolo_streamlit.py (FINAL with Heatmap + Live Dashboard FIXED)

import cv2
import streamlit as st
from detection.yolo_model import detect_objects
from dashboard.analytics import log_detections, get_summary
from alerts.telegram_bot import send_telegram_alert, send_telegram_photo
import numpy as np
import uuid
import os
import time

st.set_page_config(layout="wide")
st.title("NeuraCam - Real-Time AI Surveillance")

# Sidebar controls
camera_enabled = st.sidebar.checkbox("🎥 Enable Camera", value=True)
show_heatmap = st.sidebar.checkbox("🔥 Show Heatmap Overlay", value=False)
show_dashboard = st.sidebar.checkbox("📊 Show Live Dashboard", value=True)

# Define restricted zone
RESTRICTED_ZONE = (200, 100, 400, 300)  # (x1, y1, x2, y2)
alert_cooldown = 10  # seconds
last_alert_time = 0

# Camera setup
cap = None
if camera_enabled:
    cap = cv2.VideoCapture(0)

# Heatmap init
heatmap = np.zeros((480, 640), dtype=np.float32)
frame_placeholder = st.empty()
dashboard_placeholder = st.empty()

while camera_enabled and cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    x1, y1, x2, y2 = RESTRICTED_ZONE
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    output_frame, boxes = detect_objects(frame)

    # Check for restricted zone intrusion
    intrusion_detected = False
    for box in boxes:
        if isinstance(box[0], str):
            continue
        bx1, by1, bx2, by2 = box[:4]
        cx = int((bx1 + bx2) / 2)
        cy = int((by1 + by2) / 2)
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            intrusion_detected = True
            cv2.putText(output_frame, "⚠️ Intrusion Detected", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            boxes.append(("restricted", cx, cy))

    # Trigger alert if cooldown has passed
    current_time = time.time()
    if intrusion_detected and current_time - last_alert_time > alert_cooldown:
        filename = f"snapshot_{uuid.uuid4().hex[:8]}.jpg"
        cv2.imwrite(filename, output_frame)
        send_telegram_alert("🚨 Intrusion Detected in Restricted Zone!")
        send_telegram_photo(filename, caption="📸 Snapshot from NeuraCam")
        last_alert_time = current_time
        os.remove(filename)

    # Log detections
    log_detections(boxes)

    # Heatmap update
    for box in boxes:
        if isinstance(box[0], str):
            continue
        x1, y1, x2, y2 = box[:4]
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        if 0 <= cy < 480 and 0 <= cx < 640:
            heatmap[cy][cx] += 1

    if show_heatmap:
        heat = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
        heat = cv2.applyColorMap(heat.astype(np.uint8), cv2.COLORMAP_JET)
        output_frame = cv2.addWeighted(output_frame, 0.7, heat, 0.6, 0)

    frame_placeholder.image(output_frame, channels="BGR")

    # Live dashboard (inside loop)
    if show_dashboard:
        total, counts, df = get_summary()
        with dashboard_placeholder.container():
            st.subheader("📊 Live Analytics Dashboard")
            st.write(f"Unique Persons Detected: {total}")
            st.dataframe(df)
            st.bar_chart(counts)

cap.release()

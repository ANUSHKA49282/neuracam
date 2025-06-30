# detection/anomaly_detection.py

import time

prev_alert_time = 0
MIN_TIME_BETWEEN_ALERTS = 20

def detect_anomaly(bboxes):
    global prev_alert_time
    current_time = time.time()

    if current_time - prev_alert_time < MIN_TIME_BETWEEN_ALERTS:
        return False

    for box in bboxes:
        if isinstance(box, tuple) and box[0] == "restricted":
            prev_alert_time = current_time
            return True

    return False

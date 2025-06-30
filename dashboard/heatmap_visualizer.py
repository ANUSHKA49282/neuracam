# dashboard/heatmap_visualizer.py

import numpy as np
import cv2

# Track movement data for heatmap
heatmap_accumulator = None

def update_heatmap(frame, boxes, alpha=0.6):
    global heatmap_accumulator

    height, width = frame.shape[:2]

    if heatmap_accumulator is None:
        heatmap_accumulator = np.zeros((height, width), dtype=np.float32)

    for box in boxes:
        # Skip intrusion alerts like ("restricted", cx, cy)
        if isinstance(box[0], str):
            continue

        # Expected YOLO format: (x1, y1, x2, y2, label, conf)
        try:
            x1, y1, x2, y2 = map(int, box[:4])
            heatmap_accumulator[y1:y2, x1:x2] += 1
        except Exception as e:
            print(f"[Heatmap] Skipping invalid box {box}: {e}")
            continue

    # Normalize heatmap
    heatmap_normalized = cv2.normalize(heatmap_accumulator, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_colored = cv2.applyColorMap(heatmap_normalized.astype(np.uint8), cv2.COLORMAP_JET)

    # Blend heatmap with original frame
    overlay = cv2.addWeighted(frame, 1 - alpha, heatmap_colored, alpha, 0)

    return overlay

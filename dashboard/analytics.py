import time
import pandas as pd

detection_log = []
seen_ids = set()

def log_detections(boxes):
    """
    Log only newly seen person IDs.
    """
    now = time.time()

    for box in boxes:
        if isinstance(box[0], str):
            continue

        label = box[4]  # 'Person 1', 'Person 2' etc.

        if label not in seen_ids:
            detection_log.append((now, label))
            seen_ids.add(label)

def get_summary(last_n_seconds=60):
    now = time.time()
    recent = [(t, lbl) for (t, lbl) in detection_log if now - t <= last_n_seconds]

    df = pd.DataFrame(recent, columns=["timestamp", "label"])
    total = len(df)
    counts = df["label"].value_counts()

    return total, counts, df

# detection/tracker.py

from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize the DeepSort tracker (customize parameters as needed)
tracker = DeepSort(max_age=30)

def track_objects(frame, detections):
    """
    Takes YOLO detections and returns tracked object data with unique IDs.
    detections: [(x1, y1, x2, y2, label, conf), ...]
    """
    input_detections = []

    for det in detections:
        x1, y1, x2, y2, label, conf = det
        bbox = [x1, y1, x2 - x1, y2 - y1]  # Convert to (x, y, w, h)
        input_detections.append((bbox, conf, label))

    tracks = tracker.update_tracks(input_detections, frame=frame)

    results = []
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, w, h = track.to_ltrb()
        x1, y1, x2, y2 = int(l), int(t), int(w), int(h)
        label = track.det_class
        results.append((x1, y1, x2, y2, label, track_id))

    return results

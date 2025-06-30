from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize Deep SORT tracker
tracker = DeepSort(max_age=30)

def detect_objects(frame):
    results = model(frame)[0]
    annotated_frame = frame.copy()
    boxes = []

    detections = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = result
        label = results.names[int(cls)]

        if label != "person":
            continue  # only track people

        detections.append(([x1, y1, x2 - x1, y2 - y1], conf, label))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)

        boxes.append((x1, y1, x2, y2, f'Person {track_id}'))

        # Annotate on frame
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated_frame, f'ID: {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return annotated_frame, boxes

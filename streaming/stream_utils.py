# streaming/stream_utils.py

from streaming.multi_cam_handler import CameraStream

def start_cameras(camera_ids):
    """
    Initialize multiple CameraStream instances for given IDs.
    """
    streams = []
    for cam_id in camera_ids:
        stream = CameraStream(cam_id)
        streams.append(stream)
    return streams

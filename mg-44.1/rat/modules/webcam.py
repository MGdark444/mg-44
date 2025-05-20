import cv2
import base64
import tempfile

def take_webcam_snapshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        temp_dir = tempfile.gettempdir()
        path = os.path.join(temp_dir, "webcam.jpg")
        cv2.imwrite(path, frame)
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None
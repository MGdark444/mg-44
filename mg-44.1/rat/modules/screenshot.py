import pyautogui
import base64
import tempfile

def take_screenshot():
    temp_dir = tempfile.gettempdir()
    path = os.path.join(temp_dir, "screenshot.png")
    img = pyautogui.screenshot()
    img.save(path)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
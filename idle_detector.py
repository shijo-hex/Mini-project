# backend/detectors/idle_detector.py
import time

class IdleDetector:
    def __init__(self):
        self.last_activity = time.time()

    def update_activity(self):
        self.last_activity = time.time()

    def check_idle(self):
        if time.time() - self.last_activity > 120:  # 2 mins
            return "Warning: User idle for 2 minutes!"
        return None

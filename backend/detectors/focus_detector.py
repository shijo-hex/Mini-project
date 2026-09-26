# backend/detectors/focus_detector.py
import time
from typing import Optional

class FocusDetector:
    def __init__(self, threshold: float = 5):
        self.last_blur: Optional[float] = None
        self.threshold: float = threshold

    def record_blur(self) -> None:
        self.last_blur = time.time()

    def record_focus(self) -> Optional[str]:
        if self.last_blur is not None:
            duration = time.time() - self.last_blur
            self.last_blur = None
            if duration > self.threshold:
                return f"Alert: Tab switch/Focus loss for {duration:.2f} seconds!"
        return None

# backend/detectors/typing_detector.py
import statistics
from typing import List, Optional

class TypingDetector:
    def __init__(self, window_size: int = 20, threshold: float = 2.5):
        self.intervals: List[float] = []
        self.window_size: int = window_size
        self.threshold: float = threshold

    def record_keypress(self, interval: float) -> None:
        self.intervals.append(interval)
        if len(self.intervals) > self.window_size * 2:
            self.intervals = self.intervals[-self.window_size:]

    def detect_irregularity(self) -> Optional[str]:
        """
        Detects irregular typing style using Z-score of intervals.
        """
        if len(self.intervals) < self.window_size:
            return None
            
        mean = statistics.mean(self.intervals)
        stdev = statistics.stdev(self.intervals)
        
        if stdev == 0:
            return None
            
        latest_interval = self.intervals[-1]
        z_score = abs(latest_interval - mean) / stdev
        
        if z_score > self.threshold:
            return f"Alert: Typing anomaly detected (Z-score: {z_score:.2f})!"
        return None

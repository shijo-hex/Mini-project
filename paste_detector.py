# backend/detectors/paste_detector.py
def detect_large_paste(text):
    if len(text) > 50:  # arbitrary threshold
        return "Alert: Sudden large text pasted!"
    return None

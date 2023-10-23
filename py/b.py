import snowboydecoder
import sys
import signal

# Replace 'path/to/your/model.pmdl' with the path to your custom wake word model file
MODEL_PATH = "path/to/your/model.pmdl"

def detected_callback():
    print("Agalya detected!")  # Replace this line with your desired action

# Set the sensitivity level (between 0 and 1) based on your recording environment
sensitivity = 0.5

detector = snowboydecoder.HotwordDetector(MODEL_PATH, sensitivity=sensitivity)
print("Listening... Press Ctrl+C to exit")

# Main loop to listen for the custom wake word
detector.start(detected_callback=detected_callback,
               interrupt_check=lambda: False,
               sleep_time=0.03)

# Gracefully exit on Ctrl+C
def signal_handler(signal, frame):
    detector.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()

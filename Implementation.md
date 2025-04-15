📦 Implementation Details - Kannada Vaachaka

The following outlines the implementation phase of the Kannada Sign Language Translator project using ESP32, PAJ7620 sensor, and MediaPipe with OpenCV.

---

🛠 Hardware Setup

🔹 ESP32 Dev Board  
- Configured to receive input from the PAJ7620 gesture sensor  
- Connected via USB to the laptop for serial communication

🔹 PAJ7620 Gesture Sensor  
- Recognizes up to 9 hand gestures  
- Communicates via I2C with the ESP32 board

🔹 Laptop Webcam  
- Used for real-time gesture recognition using OpenCV + MediaPipe

---

🧠 Software Setup

🔹 Arduino IDE  
- Programmed the ESP32 to interface with PAJ7620  
- Serially transmits recognized gesture data to the Python script

🔹 Python Libraries Used:
- opencv-python → for webcam input and visualization  
- mediapipe → for real-time hand gesture recognition  
- pygame / playsound → to play Kannada audio  
- pyserial → to read data from ESP32 via serial

---

🧩 System Workflow

1. **Sensor-Based Gesture Detection**
   - ESP32 reads gesture data from PAJ7620
   - Sends gesture code to the laptop via Serial

2. **Webcam Gesture Verification**
   - Python + MediaPipe recognizes the same gesture from webcam input
   - If both sensor and webcam detect the same gesture ➜ Validation Success

3. **Audio Output**
   - Corresponding Kannada audio file (e.g., namaskara.mp3) is played
   - Ensures real-time response and communication

---

🔁 Loop Flow (Python Snippet)

```python
if serial_input == "up" and mediapipe_gesture == "up":
    play_audio("audio/namaskara.mp3")
elif serial_input == "down" and mediapipe_gesture == "down":
    play_audio("audio/yesu.mp3")
# ... and so on for other gestures

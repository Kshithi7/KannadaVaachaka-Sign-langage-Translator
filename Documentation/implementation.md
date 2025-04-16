# 🛠️ Kannada Vaachaka – Implementation Guide

This file documents the complete procedure followed to build the real-time Kannada Sign Language Translator using **ESP32**, **PAJ7620 gesture sensor**, and **OpenCV + MediaPipe** in Python.

---
## 🛣️ Initial Idea: Flex Sensors

Initially, the project was planned using **Flex Sensors** for gesture detection. The idea was to attach flex sensors on fingers to measure the degree of bending, allowing identification of specific hand poses.

### 🔌 Flex Sensor Connection Diagram
*A wiring diagram showing how each flex sensor would connect to the microcontroller.*

> If u want to use flex sensor, then go through the images folder for circuit diagram and connection of flex sensors.

### ❌ Why It Was Changed

However, due to **unavailability of flex sensors**, this idea was dropped. Instead, we switched to:

- **PAJ7620 gesture recognition sensor** (for 9 gestures)
- **MediaPipe + OpenCV** (for finger detection)

This transition allowed for **non-contact** and **camera-based** recognition, making the system more hygienic, accessible, and cost-efficient.

---

## 🧠 Step-by-Step Implementation

### 1️⃣ Initial Planning & Documentation

Before jumping into development, the following planning was done:

- ✅ Listed out commonly used Kannada sign gestures.
- ✅ Mapped each gesture to:
  - A **Kannada translated text**
  - A **Kannada audio file** (e.g., `namaskara.mp3`)
- ✅ Created a document to maintain a mapping table for Gesture ➜ Text ➜ Audio.

---

### 2️⃣ Software Installation & Setup

To begin the development, the essential software and libraries were installed.
---

#### 📌 Python Setup

- Install **Python IDLE** from [python.org](https://www.python.org/downloads/)
- Make sure Python is added to system PATH.
- Check version:  
  ```bash
  python --version
  
 ----
 
####📌 Required Python Libraries
Install the following packages:

pip install opencv-python
pip install mediapipe
pip install pygame
pip install pyserial
pip install pyaudio

💡 Make sure to check compatibility for your Python version, especially for pyaudio.
 ---
 
📌 ESP32 Setup
- Install the ESP32 board in the Arduino IDE via the board manager.
- Connect ESP32 to the laptop via USB.
- Upload code to read gestures from PAJ7620 sensor and send data over Serial.

 ---
 
3️⃣ Project Folder Structure
-Organize your project directory like this:

KannadaVaachaka/
│
├── main.py
├── esp32_code.ino
├── /audio/
│   ├── namaskara.mp3
│   ├── hegiddira.mp3
│   └── ...
├── /docs/
│   └── implementation.md

---

4️⃣ Linking Audio to Gestures
Each recognized gesture corresponds to a Kannada audio file.
Example logic in Python:

if gesture == "up":
    play_audio("audio/namaskara.mp3")
elif gesture == "down":
    play_audio("audio/hegiddira.mp3")
# and so on...
- Ensure that all .mp3 files are inside the /audio/ folder and named clearly.

---

5️⃣ Python Code – Main Flow
The Python code:
--Reads gesture input via Serial from ESP32 + PAJ7620 sensor.
--Uses MediaPipe with OpenCV to recognize webcam gestures.
--If both sensor and webcam detect the same gesture → Trigger Kannada audio.

if serial_input == "up" and mediapipe_gesture == "up":
    play_audio("audio/namaskara.mp3")

---

6️⃣ Sensor Function Code (ESP32 + PAJ7620)
The ESP32 is programmed using Arduino IDE to:
 - Communicate with PAJ7620 over I2C
 -Detect gestures and send simplified values (up, down, etc.) to Python via Serial

---

7️⃣ Testing & Debugging
Each module was tested individually and then together:

✅ ESP32 + PAJ7620 sensor tested for gesture recognition

✅ Webcam tested using OpenCV + MediaPipe

✅ Audio tested for playback with correct triggers

✅ Dual verification of gestures ensured higher accuracy

✅ Latency was maintained under 1 second
---

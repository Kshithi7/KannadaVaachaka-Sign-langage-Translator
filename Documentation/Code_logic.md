# 🧠 Code Logic – Kannada Vāchakā: Sign Language Translator

## 🎯 Goal
To create a real-time sign language translator that detects hand gestures and converts them into Kannada speech, enabling communication for individuals with speech and hearing impairments.

---

## 🔧 Hardware and Software Used
- ESP32 Devkit (gesture signal acquisition via PAJ7620)
- PAJ7620 Gesture Recognition Sensor
- Raspberry Pi 4 / Laptop (data processing)
- OpenCV + MediaPipe (visual recognition + verification)
- Pygame (for Kannada speech output)
- Python + Arduino IDE

---

## 🧩 Logic Breakdown

### 1. **Gesture Acquisition**
- **Sensor Input**: PAJ7620 detects 9 types of gestures (e.g., Up, Down, Left, Right).
- **OpenCV + MediaPipe**: Detects number of fingers raised using hand landmarks.
- Data is transmitted via Serial or WiFi from ESP32 to Raspberry Pi/Laptop.

### 2. **Processing & Classification**
- MediaPipe extracts key hand landmarks (fingertips, wrist, etc.).
- Number of fingers raised is mapped to specific Kannada words:
  - 1 finger = Namaskara
  - 2 fingers = Naanu
  - 3 fingers = Neenu
  - ...
- PAJ7620 gesture outputs are mapped similarly to Kannada actions:
  - Up = Yestu, Down = Neeru, Left = Sahaya, etc.

### 3. **Output Generation**
- Detected gestures are classified in real time.
- Corresponding `.mp3` files are played using `pygame.mixer` for Kannada voice output.
- Output also displayed on OpenCV video frame using `cv2.putText()`.

---

## 🔄 Communication Flow
- PAJ7620 → ESP32 via **I2C**
- ESP32 → Raspberry Pi/Laptop via **Serial** or **Wi-Fi**
- Camera feed processed using **MediaPipe + OpenCV**

---

## 📌 Output Behavior
- Gesture appears as bounding box with Kannada text on screen.
- Real-time Kannada audio plays for each recognized gesture.
- Serial Monitor logs each detected gesture for debugging.

---

## 💬 Notes
- Pygame ensures non-blocking audio playback.
- MediaPipe + PAJ7620 gives double-verification to boost accuracy.
- System designed for **expandability** – more gestures & languages can be added later.

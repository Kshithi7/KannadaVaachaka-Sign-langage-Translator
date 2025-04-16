import serial import time import cv2
import mediapipe as mp import pygame pygame.mixer.init()
# Serial Port Setup
#port = '/dev/ttyUSB0' #	Use
'/dev/serial0' or '/dev/ttyS0' for Raspberry Pi UART port port = 'COM9' #	windows
baud_rate = 9600 # Must match the baud rate used in your device timeout = 1 # Timeout for serial communication in seconds
try:
# Open the serial port
ser = serial.Serial(port, baud_rate, timeout=timeout) print(f"Connected to {port} at {baud_rate} baud rate.") time.sleep(2) # Wait for 2 seconds to ensure the connection is established
except serial.SerialException as e: print(f"Error: {e}")
ser = None
# MediaPipe Hands Setup mp_hands = mp.solutions.hands mp_drawing = mp.solutions.drawing_utils
# Initialize video capture cap = cv2.VideoCapture(0) # Hand detection function
def count_fingers(hand_landmarks):
fingertips_ids = [4, 8, 12, 16, 20] # List of landmark indices corresponding to fingertips
wrist = hand_landmarks.landmark[0] # Wrist landmark fingers = []
for idx in fingertips_ids:
tip_y = hand_landmarks.landmark[idx].y
dip_y = hand_landmarks.landmark[idx - 2].y # DIP joint below the fingertip
if tip_y < dip_y: # Check if fingertip is above the DIP joint (finger is raised)
 
fingers.append(1) else:
fingers.append(0) 41
# For thumb, check the x-axis direction compared to the hand palm center
thumb_tip = hand_landmarks.landmark[4] thumb_ip
= hand_landmarks.landmark[3]
if thumb_tip.x < thumb_ip.x: # Left hand thumb is to the left of IP joint
fingers[0] = 1 else:
fingers[0] = 0
return sum(fingers) # Return the count of raised fingers try:
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
while cap.isOpened():
ret, frame = cap.read() if not ret:
break
frame = cv2.flip(frame, 1) # Flip for a mirror effect
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Convert to RGB
results = hands.process(rgb_frame) # Process frame for hand landmarks
if results.multi_hand_landmarks:
for hand_landmarks in results.multi_hand_landmarks: mp_drawing.draw_landmarks(frame,
hand_landmarks, mp_hands.HAND_CONNECTIONS) # Draw landmarks h, w, _ = frame.shape
x_min = min([lm.x for lm in
hand_landmarks.landmark]) * w x_max = max([lm.x for lm in hand_landmarks.landmark]) * w y_min = min([lm.y for lm in
hand_landmarks.landmark]) * h y_max = max([lm.y for lm in hand_landmarks.landmark]) * h cv2.rectangle(frame, (int(x_min),
int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2) # Draw bounding box
fingers_count = count_fingers(hand_landmarks) # Count raised fingers
message = ""
if fingers_count == 1:
message = "namaskara" if message:
cv2.putText(frame, message, (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif fingers_count == 2:
message = "Naanu" if message:
cv2.putText(frame, message, (int(x_min), int(y_min) - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif fingers_count == 3:
message = "Neenu" if message:
cv2.putText(frame, message, (int(x_min), int(y_min) - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif fingers_count == 4:
 message = "Chanagidiya" if message:
cv2.putText(frame, message, (int(x_min), int(y_min) - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif fingers_count == 5: message = "Oota" if message:
cv2.putText(frame, message, (int(x_min), int(y_min) - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
time.sleep(2)
if ser and ser.in_waiting > 0: # Check if there is data to be read from the serial port
try:
data = ser.readline().decode('utf-8', errors='ignore').strip()
if data: # Only process non-empty decoded data print(f"Gesture Detected from Sensor")
if data == "Up":
print("Task: Yestu") 
mp3_file = "<audio path> " pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "Down":
print("Task: Neeru")
mp3_file = "<audio path>"
elif data == "Left":
print("Task: Sahaya") 
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "Right":
print("Task: Mane")
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "Forward":
print("Task: Showchalaya") mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "Backward":
print("Task: Kelasa") 
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "Clockwise":
print("Task: Dhanyavaadha") 
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
elif data == "anti-clockwise": print("Task: Appa")
mp3_file = "<audio path>"
elif data == "wave":
print("Task: Amma")
mp3_file = "<audio path>" pygame.mixer.music.load(mp3_file) pygame.mixer.music.play()
else:
print("No task assigned for this gesture") time.sleep(2)
except serial.SerialException as e: print(f"Serial read error: {e}")
cv2.imshow('Hand Gesture Message Display', frame) # Display frame
if cv2.waitKey(10) & 0xFF == ord('q'): # Break the loop when 'q' is pressed
break except
KeyboardInterrupt:
print("\nExiting...")
finally:
if 'ser' in locals() and ser and ser.is_open: ser.close() print("Serial connection closed.")
cap.release() # Release video capture cv2.destroyAllWindows() # Close all OpenCV windows

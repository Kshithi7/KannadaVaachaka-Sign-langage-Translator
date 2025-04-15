import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

# Hand detection function
def count_fingers(hand_landmarks):
    # List of landmark indices corresponding to fingertips
    fingertips_ids = [4, 8, 12, 16, 20]

    # Get landmarks for wrist and fingertips
    wrist = hand_landmarks.landmark[0]
    
    # Count fingers raised
    fingers = []
    for idx in fingertips_ids:
        tip_y = hand_landmarks.landmark[idx].y
        dip_y = hand_landmarks.landmark[idx - 2].y  # DIP joint below the fingertip

        # Check if fingertip is above the DIP joint (finger is raised)
        if tip_y < dip_y:
            fingers.append(1)
        else:
            fingers.append(0)

    # For thumb, check the x-axis direction compared to the hand palm center
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    if thumb_tip.x < thumb_ip.x:
        fingers[0] = 1
    else:
        fingers[0] = 0

    # Return the count of raised fingers
    return sum(fingers)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB as Mediapipe processes RGB images
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for hand landmarks
        results = hands.process(rgb_frame)

        # If hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections on the hand
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the bounding box coordinates
                h, w, _ = frame.shape
                x_min = min([lm.x for lm in hand_landmarks.landmark]) * w
                x_max = max([lm.x for lm in hand_landmarks.landmark]) * w
                y_min = min([lm.y for lm in hand_landmarks.landmark]) * h
                y_max = max([lm.y for lm in hand_landmarks.landmark]) * h

                # Draw the bounding box
                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)

                # Count raised fingers
                fingers_count = count_fingers(hand_landmarks)

                # Display the finger count on the frame
                cv2.putText(frame, f'Fingers: {fingers_count}', (int(x_min), int(y_min) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Hand Gesture Number Detection', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

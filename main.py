import cv2
import mediapipe as mp
import time
import winsound  # Works on Windows for the beep
from dms_utils import calculate_ear, LEFT_EYE_IDXS, RIGHT_EYE_IDXS

# Configuration
EAR_THRESHOLD = 0.21      # If EAR is below this, eyes are closed
DROWSY_TIME_LIMIT = 1   # Seconds before beep starts
ALARM_FREQUENCY = 1000    # Hertz
ALARM_DURATION = 500      # Milliseconds

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
eye_closed_start_time = None

print("System Starting... Press 'ESC' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # Flip frame for a mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        coords = [(int(l.x * w), int(l.y * h)) for l in landmarks]
        
        # Calculate EAR
        left_ear = calculate_ear(LEFT_EYE_IDXS, coords)
        right_ear = calculate_ear(RIGHT_EYE_IDXS, coords)
        avg_ear = (left_ear + right_ear) / 2.0

        # Drowsiness Logic
        if avg_ear < EAR_THRESHOLD:
            if eye_closed_start_time is None:
                eye_closed_start_time = time.time()
            
            duration = time.time() - eye_closed_start_time
            if duration >= DROWSY_TIME_LIMIT:
                # Trigger Laptop Beep
                winsound.Beep(ALARM_FREQUENCY, ALARM_DURATION)
                cv2.putText(frame, "DROWSINESS ALERT!", (50, 200), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        else:
            eye_closed_start_time = None

        # Display EAR value for debugging
        color = (0, 255, 0) if avg_ear > EAR_THRESHOLD else (0, 0, 255)
        cv2.putText(frame, f"EAR: {avg_ear:.2f}", (20, 50), 0, 0.7, color, 2)

    cv2.imshow('Driver Monitor (Laptop Test)', frame)
    
    if cv2.waitKey(5) & 0xFF == 27: # Press Esc
        break

cap.release()
cv2.destroyAllWindows()
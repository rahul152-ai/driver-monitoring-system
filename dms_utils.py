import numpy as np

def calculate_ear(eye_landmarks, landmarks):
    """Calculates the Eye Aspect Ratio (EAR)"""
    # Vertical distances (p2-p6, p3-p5)
    p2_p6 = np.linalg.norm(np.array(landmarks[eye_landmarks[1]]) - np.array(landmarks[eye_landmarks[5]]))
    p3_p5 = np.linalg.norm(np.array(landmarks[eye_landmarks[2]]) - np.array(landmarks[eye_landmarks[4]]))
    
    # Horizontal distance (p1-p4)
    p1_p4 = np.linalg.norm(np.array(landmarks[eye_landmarks[0]]) - np.array(landmarks[eye_landmarks[3]]))
    
    ear = (p2_p6 + p3_p5) / (2.0 * p1_p4)
    return ear

# Mediapipe Face Mesh Indices for Eyes
LEFT_EYE_IDXS = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_IDXS = [33, 160, 158, 133, 153, 144]
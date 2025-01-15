import cv2
import mediapipe as mp
from ultralytics import YOLO
import math

# Paths to models
fire_model_path = 'fire_detection_model.pt'  # Trained model for fire detection
human_model_path = 'yolov8n.pt'             # Pre-trained YOLOv8 model for human detection

# Load models
fire_model = YOLO(fire_model_path)  # Trained fire detection model
human_model = YOLO(human_model_path)  # Pre-trained YOLOv8 model for humans

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    """Calculates the angle at point b (in degrees)."""
    angle = math.degrees(
        math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x)
    )
    return abs(angle if angle >= 0 else 360 + angle)

# Function to determine posture based on keypoints
def analyze_posture(landmarks):
    try:
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
        left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]

        # Calculate angles
        hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)
        ankle_angle = calculate_angle(left_hip, left_knee, left_ankle)

        # Posture classification
        if hip_angle > 160:
            return "Standing"
        elif 90 < hip_angle <= 160:
            return "Sitting"
        elif ankle_angle < 45:
            return "Fallen Down"
        else:
            return "Unknown Posture"
    except Exception as e:
        return "Error"

# Paths to input video and output video
video_path = 'input_vid2_highres.mp4'  # Input video file
output_video_path = 'output_posture.mp4'  # Output video file

# Initialize video capture and output
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, 20.0,
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

# Define colors for bounding boxes
COLOR_FIRE = (0, 0, 255)   # Red for fire
COLOR_HUMAN = (0, 255, 0)  # Green for humans
COLOR_POSTURE = (255, 0, 0)  # Blue for posture

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Fire detection
    fire_results = fire_model.predict(frame)[0]  # Extract fire detection results

    # Human detection
    human_results = human_model.predict(frame)[0]  # Extract human detection results

    # Process fire detection results
    for box in fire_results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
        confidence = box.conf[0]  # Confidence score
        class_id = int(box.cls[0])  # Class ID
        label = fire_results.names[class_id]  # Class name

        if label == 'fire':  # Check for the 'fire' class
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_FIRE, 2)
            cv2.putText(frame, f'Fire: {confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_FIRE, 2)

    # Process human detection results
    for box in human_results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
        confidence = box.conf[0]  # Confidence score
        class_id = int(box.cls[0])  # Class ID
        label = human_results.names[class_id]  # Class name

        if label == 'person':  # Check for the 'person' class
            cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_HUMAN, 2)
            cv2.putText(frame, f'Person: {confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_HUMAN, 2)

            # Crop detected human region
            cropped_frame = frame[y1:y2, x1:x2]

            # Convert cropped frame to RGB for MediaPipe
            rgb_cropped = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)
            pose_results = pose.process(rgb_cropped)

            # Check if landmarks detected
            if pose_results.pose_landmarks:
                # Draw pose on cropped region
                mp_drawing.draw_landmarks(
                    cropped_frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS
                )

                # Analyze posture
                posture = analyze_posture(pose_results.pose_landmarks.landmark)

                # Display posture on original frame
                cv2.putText(
                    frame,
                    posture,
                    (x1, y2 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    COLOR_POSTURE,
                    1,
                    cv2.LINE_AA,
                )

    # Write the processed frame to the output video
    out.write(frame)

    # Display the frame in a window
    cv2.imshow('YOLO Fire and Human Detection with Posture Analysis', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processing complete. Video saved as '{output_video_path}'.")

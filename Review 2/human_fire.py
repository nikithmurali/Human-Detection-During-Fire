import cv2
from ultralytics import YOLO

# Paths to models
fire_model_path = 'fire_detection_model.pt'  # Trained model for fire detection
human_model_path = 'yolov8n.pt'             # Pre-trained YOLOv8 model for human detection

# Load models
fire_model = YOLO(fire_model_path)  # Trained fire detection model
human_model = YOLO(human_model_path)  # Pre-trained YOLOv8 model for humans

# Paths to input video and output video
video_path = 'input_vid2.mp4'  # Input video file
output_video_path = 'output_combined_video.mp4'  # Output video file

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

    # Write the processed frame to the output video
    out.write(frame)

    # Display the frame in a window
    cv2.imshow('YOLO Fire and Human Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processing complete. Video saved as '{output_video_path}'.")















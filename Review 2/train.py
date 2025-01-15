import os
from ultralytics import YOLO
import zipfile
import cv2

# Path to the uploaded zip file (update with your local path)
uploaded_zip_path = r'C:\Users\farde\capstone\Fire Detection.v1i.yolov8.zip'
extracted_path = r'C:\Users\farde\capstone\dataset'  # Adjusted for local system

# Extract the uploaded zip file
with zipfile.ZipFile(uploaded_zip_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_path)

# Verify paths
train_folder = os.path.join(extracted_path, 'train')
images_path = os.path.join(train_folder, 'images')
labels_path = os.path.join(train_folder, 'labels')

# Verify if images and labels directories exist
if not os.path.exists(images_path) or not os.path.exists(labels_path):
    raise FileNotFoundError(f"Could not find 'images' or 'labels' in {train_folder}")

# Check label files format and find unique class IDs
unique_class_ids = set()
for label_file in os.listdir(labels_path):
    if label_file.endswith('.txt'):
        with open(os.path.join(labels_path, label_file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) != 5:
                    raise ValueError(f"Incorrect label format in file {label_file}: {line}")

                # Add class ID to the set
                unique_class_ids.add(int(parts[0]))

# Create dataset.yaml with all identified classes
dataset_yaml = os.path.join(train_folder, 'dataset.yaml')
with open(dataset_yaml, 'w') as f:
    f.write(f"path: {train_folder}\n")
    f.write("train: images\n")
    f.write("val: images\n")
    f.write("names:\n")

    # Write class names based on unique class IDs
    for class_id in sorted(list(unique_class_ids)):
        if class_id == 0:
            f.write(f"  {class_id}: fire\n")  # Assuming class 0 is 'fire'
        elif class_id == 1:
            f.write(f"  {class_id}: smoke\n")  # Assuming class 1 is 'smoke'
        elif class_id == 2:
            f.write(f"  {class_id}: person\n")  # Assuming class 2 is 'person'
        # Add more elif blocks for other potential classes as needed

# Train YOLO model
model = YOLO('yolov8n.pt')  # Load the pre-trained YOLOv8 nano model

model.train(
    data=dataset_yaml,
    epochs=10,
    imgsz=640,
    batch=8,
    workers=2
)

# Save the fine-tuned model
model.save('fire_detection_model.pt')
print("Training complete. Model saved as 'fire_detection_model.pt'.")
import os
from ultralytics import YOLO

# Load a pre-trained YOLO model
model = YOLO("./YOLOV11m/weights/best.pt")
# Define the input and output directories
input_folder = "./test_images"
output_folder = "./res"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".webp")):  # Adjust for supported image formats
        image_path = os.path.join(input_folder, filename)

        # Perform object detection on the image
        results = model(image_path)

        # Save the result image with bounding boxes to the output folder
        output_path = os.path.join(output_folder, filename)
        results[0].save(output_path)

        print(f"Processed {filename} and saved to {output_path}")

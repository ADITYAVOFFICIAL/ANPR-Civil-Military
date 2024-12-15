from ultralytics import YOLO
import cv2
import os
from pathlib import Path
from PIL import Image
import imagehash

# Load the YOLOv8 model
model = YOLO('latest.pt')

# Set confidence threshold
conf_threshold = 0.9

# Create directory to save detected license plates
output_dir = 'license_plates'
os.makedirs(output_dir, exist_ok=True)

# Open video file
video_path = 'test_videos/toll.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

frame_count = 0
detections = []

# Perform YOLO object detection and save images
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process every 10th frame
    if frame_count % 10 == 0:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Iterate over detected objects
        for detection in results[0].boxes:
            # Extract bounding box coordinates and confidence
            xmin, ymin, xmax, ymax = detection.xyxy[0].tolist()
            confidence = detection.conf[0].item()
            
            if confidence > conf_threshold:
                # Convert coordinates to integers
                xmin, ymin, xmax, ymax = map(int, [xmin, ymin, xmax, ymax])
                
                # Extract the bounding box
                bbox = frame[ymin:ymax, xmin:xmax]

                # Save the bounding box image
                save_path = os.path.join(output_dir, f'plate_{frame_count}_{confidence:.2f}.jpg')
                cv2.imwrite(save_path, bbox)

                # Track detections
                detections.append((frame_count, xmin, ymin, xmax, ymax, confidence))

    frame_count += 1

# Release the video capture object
cap.release()
cv2.destroyAllWindows()

def image_similarity(img1_path, img2_path):
    """Calculate the hash similarity between two images."""
    hash1 = imagehash.average_hash(Image.open(img1_path))
    hash2 = imagehash.average_hash(Image.open(img2_path))
    return hash1 - hash2  # Return the Hamming distance between hashes

def find_similar_images(image_folder, threshold=10):
    """Find and remove very similar images, keeping only the clearest version."""
    image_paths = list(Path(image_folder).glob('*.[pj][np]g'))
    to_remove = set()

    for i, img_path in enumerate(image_paths):
        if img_path in to_remove:
            continue
        for j, other_img_path in enumerate(image_paths):
            if i != j and other_img_path not in to_remove:
                similarity = image_similarity(img_path, other_img_path)
                if similarity <= threshold:
                    # Keep the image with the highest resolution
                    if os.path.getsize(img_path) < os.path.getsize(other_img_path):
                        to_remove.add(img_path)
                    else:
                        to_remove.add(other_img_path)
    
    # Remove similar images
    for img_path in to_remove:
        print(f"Removing {img_path}")
        os.remove(img_path)

if __name__ == "__main__":
    find_similar_images(output_dir)

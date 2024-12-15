import cv2
import numpy as np
from paddleocr import PaddleOCR
import logging
import matplotlib.pyplot as plt

# Set the logging level to suppress debug messages
logging.getLogger('ppocr').setLevel(logging.WARNING)  # Only show warning and above

"""
Paddle OCR
"""
def ocr_with_paddle(img_path):
    finaltext = ''
    # Initialize PaddleOCR with use_gpu set to True
    ocr = PaddleOCR(lang='en', use_angle_cls=True, use_cpu=True)  # Set use_gpu=False for M1 compatibility
    
    # Read the image from the provided path
    img_cv2 = cv2.imread(img_path)  # Load the image using OpenCV
    if img_cv2 is None:
        raise ValueError(f"Image not found at the path: {img_path}")

    # Preprocessing: Convert to grayscale and apply thresholding
    gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Perform OCR
    result = ocr.ocr(img_cv2, cls=True)
    
    # Annotate the image with detected text
    for line in result:
        for word_info in line:
            box = np.array(word_info[0])  # Get the bounding box
            text = word_info[1][0]  # Extract the text from the OCR result
            
            # Ignore "IND"
            if "IND" in text:
                continue
            
            finaltext += ' ' + text  # Append to final text
            
            # Draw bounding box
            cv2.polylines(img_cv2, [np.int32(box)], isClosed=True, color=(0, 255, 0), thickness=2)
            
            # Calculate the position for the text
            x, y = int(box[0][0]), int(box[0][1] - 10)
            
            # Create a background for the text
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
            cv2.rectangle(img_cv2, (x, y - text_size[1] - 5), (x + text_size[0], y + 5), (255, 255, 255), -1)  # White background
            
            # Put the text on the image
            cv2.putText(img_cv2, text, (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)  # Black text

    return finaltext.strip(), img_cv2  # Return the extracted text and annotated image

"""
Main function to execute the OCR
"""
if __name__ == "__main__":
    image_path = "./license_plates/plate_440_0.89.jpg"  # Specify the image path
    try:
        extracted_text, annotated_image = ocr_with_paddle(image_path)  # Perform OCR on the image
        print("Extracted Text:")
        print(extracted_text)  # Print the extracted text
        
        # Display the annotated image using matplotlib
        plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')  # Turn off axis labels
        plt.show()  # Show the image
    except Exception as e:
        print(f"An error occurred: {e}")

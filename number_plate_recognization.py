# Module: vehicle_plate_recognition.py
import cv2
import pytesseract

def recognize_plate(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plate_text = pytesseract.image_to_string(grayscale_image, config='--psm 8')
    return plate_text.strip()

# Usage
sample_image_path = metadata.iloc[0]['vehicle_image_path']
recognized_plate = recognize_plate(sample_image_path)
print(f"Recognized Plate: {recognized_plate}")

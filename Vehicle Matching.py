import cv2
import pytesseract
import pandas as pd

def recognize_license_plate(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_plate = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    license_plate_text = pytesseract.image_to_string(binary_plate, config='--psm 8')
    return license_plate_text.strip()

def match_license_plate(metadata, approved_vehicles):
    matched_records = []
    for idx, row in metadata.iterrows():
        license_plate_image_path = row['license_plate_image_path']
        license_plate_text = recognize_license_plate(license_plate_image_path)
        
        if license_plate_text in approved_vehicles:
            matched_records.append(row)
    
    return pd.DataFrame(matched_records)

# Usage
data_dir = "realtime_vehicle_data"
metadata = load_metadata(data_dir)
approved_vehicles = ["ABC123", "XYZ789"]  # Example approved vehicle plates
matched_vehicles = match_license_plate(metadata, approved_vehicles)
print(matched_vehicles)

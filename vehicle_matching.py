# Module: vehicle_matching.py
import pytesseract
from pytesseract import Output

def recognize_license_plate(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary_plate = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    license_plate_text = pytesseract.image_to_string(binary_plate, config='--psm 8')  # PSM 8 for single word recognition
    return license_plate_text.strip()

def match_vehicle(license_plate_text, approved_db):
    return approved_db.get(license_plate_text, "Unauthorized")

# Usage
approved_db = {"ABC123": "Authorized", "XYZ789": "Unauthorized"}
image_path = metadata.iloc[0]['vehicle_image_path']
license_plate_text = recognize_license_plate(image_path)
status = match_vehicle(license_plate_text, approved_db)
print(f"License Plate: {license_plate_text}, Status: {status}")

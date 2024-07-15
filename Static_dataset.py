import os
import cv2
from datetime import datetime

def create_static_dataset(dataset_dir):
    os.makedirs(dataset_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)
    
    print("Press 's' to save an image, 'q' to quit")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            plate_number = input("Enter the vehicle plate number: ")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(dataset_dir, f"{plate_number}_{timestamp}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Saved {image_path}")
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Usage
static_dataset_dir = "static_vehicle_dataset"
create_static_dataset(static_dataset_dir)

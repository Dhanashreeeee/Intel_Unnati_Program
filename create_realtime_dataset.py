import cv2
import os
import datetime

def capture_image(camera_index, save_dir, prefix):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join(save_dir, f"{prefix}_{timestamp}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Captured image saved to {image_path}")
        return image_path, timestamp
    else:
        print("Error: Could not read frame.")
        return None, None
    
    cap.release()

def create_metadata_file(image_path, timestamp, metadata_path, prefix):
    with open(metadata_path, 'a') as f:
        f.write(f"{prefix}_image_path: {image_path}\n")
        f.write(f"{prefix}_timestamp: {timestamp}\n")

def create_realtime_dataset(save_dir, num_images, camera_index=0):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    metadata_path = os.path.join(save_dir, "metadata.txt")
    with open(metadata_path, 'w') as f:
        f.write("")  # Create or clear the file

    for i in range(num_images):
        vehicle_image_path, vehicle_timestamp = capture_image(camera_index, save_dir, 'vehicle')
        license_plate_image_path, license_plate_timestamp = capture_image(camera_index, save_dir, 'license_plate')
        if vehicle_image_path and license_plate_image_path:
            create_metadata_file(vehicle_image_path, vehicle_timestamp, metadata_path, 'vehicle')
            create_metadata_file(license_plate_image_path, license_plate_timestamp, metadata_path, 'license_plate')

# Usage
save_dir = "realtime_vehicle_data"
num_images = 10
create_realtime_dataset(save_dir, num_images)

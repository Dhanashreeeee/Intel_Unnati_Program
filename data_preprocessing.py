import cv2
import pandas as pd
import numpy as np
import os

def resize_and_grayscale(image_path):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (640, 480))
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def preprocess_images(metadata):
    for idx, row in metadata.iterrows():
        vehicle_image_path = row['vehicle_image_path']
        license_plate_image_path = row['license_plate_image_path']
        
        if os.path.exists(vehicle_image_path) and os.path.exists(license_plate_image_path):
            vehicle_image = resize_and_grayscale(vehicle_image_path)
            license_plate_image = resize_and_grayscale(license_plate_image_path)
            
            # Save the processed images
            cv2.imwrite(vehicle_image_path, vehicle_image)
            cv2.imwrite(license_plate_image_path, license_plate_image)
        else:
            print(f"Missing image file: {vehicle_image_path} or {license_plate_image_path}")

# Usage
data_dir = "realtime_vehicle_data"
metadata = load_metadata(data_dir)
preprocess_images(metadata)

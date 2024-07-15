# Module: load_dataset.py
import pandas as pd
import cv2
import os

def load_metadata(data_dir):
    records = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".jpg"):
            plate_number, timestamp = filename.split('_')[:2]
            records.append({
                'vehicle_image_path': os.path.join(data_dir, filename),
                'timestamp': timestamp,
                'plate_number': plate_number
            })
    return pd.DataFrame(records)

def display_sample_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('Sample Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
data_dir = "static_vehicle_dataset"
metadata = load_metadata(data_dir)
print(metadata.head())
display_sample_image(metadata.iloc[0]['vehicle_image_path'])

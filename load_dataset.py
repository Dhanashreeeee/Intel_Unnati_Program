import os
import pandas as pd
import cv2
import datetime

def load_metadata(data_dir):
    records = []
    metadata_file = os.path.join(data_dir, "metadata.txt")
    if not os.path.exists(metadata_file):
        print("Metadata file not found.")
        return pd.DataFrame(records)
    
    with open(metadata_file, 'r') as f:
        metadata = {}
        for line in f:
            key, value = line.strip().split(": ")
            if key.endswith('_timestamp'):
                value = datetime.datetime.strptime(value, "%Y%m%d_%H%M%S")
            metadata[key] = value
        
        for i in range(len(metadata) // 4):  # Assuming 4 entries per record (2 images, 2 timestamps)
            record = {
                'vehicle_image_path': metadata[f'vehicle_image_path_{i}'],
                'vehicle_timestamp': metadata[f'vehicle_timestamp_{i}'],
                'license_plate_image_path': metadata[f'license_plate_image_path_{i}'],
                'license_plate_timestamp': metadata[f'license_plate_timestamp_{i}']
            }
            records.append(record)
    
    return pd.DataFrame(records)

def display_sample_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('Sample Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
data_dir = "realtime_vehicle_data"
metadata = load_metadata(data_dir)
print(metadata.head())
display_sample_image(metadata.iloc[0]['vehicle_image_path'])

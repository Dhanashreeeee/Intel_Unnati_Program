# Module: load_dataset.py
import os
import pandas as pd
import cv2

def load_metadata(data_dir):
    records = []
    for filename in os.listdir(data_dir):
        if filename.endswith("_metadata.txt"):
            with open(os.path.join(data_dir, filename), 'r') as f:
                metadata = {}
                for line in f:
                    key, value = line.strip().split(": ")
                    metadata[key] = value
                records.append(metadata)
    return pd.DataFrame(records)

def display_sample_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('Sample Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
data_dir = "data/vehicle_images"
metadata = load_metadata(data_dir)
print(metadata.head())
display_sample_image(metadata.iloc[0]['vehicle_image_path'])

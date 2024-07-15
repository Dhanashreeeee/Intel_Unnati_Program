# Module: data_preprocessing.py
import cv2
import pandas as pd

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def preprocess_metadata(metadata):
    metadata['timestamp'] = pd.to_datetime(metadata['timestamp'], format='%Y%m%d_%H%M%S')
    return metadata

# Usage
metadata = preprocess_metadata(metadata)
sample_image = preprocess_image(metadata.iloc[0]['vehicle_image_path'])
cv2.imshow('Preprocessed Image', sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

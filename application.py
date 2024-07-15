# Module: app.py
from flask import Flask, render_template, request
import pandas as pd
import cv2
import pytesseract

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        image_path = f"static/uploads/{file.filename}"
        file.save(image_path)

        plate_number = recognize_plate(image_path)
        update_dynamic_datasets(plate_number, entry_dataset_path, exit_dataset_path, action='entry')
        return f"Recognized Plate: {plate_number}"

if __name__ == '__main__':
    app.run(debug=True)

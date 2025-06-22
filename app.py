from flask import Flask, request, jsonify, render_template, send_file
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# Inisialisasi Flask
app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model YOLOv8 hasil training
model = YOLO("color-detector/yolov8-color-v3/weights/best.pt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil file dari form
    file = request.files['image']
    test_image_path = os.path.join(app.config['UPLOAD_FOLDER'], "input.jpg")
    file.save(test_image_path)

    # Lakukan deteksi objek warna dengan YOLO
    results = model(test_image_path, save=True, show=False)

    # Ambil hasil deteksi (label dan confidence)
    predictions = []
    validation_message = ""
    
    for result in results:
        # Cek apakah ada deteksi
        if result.boxes is None or len(result.boxes) == 0:
            validation_message = "Tidak ada warna yang terdeteksi dalam gambar. Pastikan gambar memiliki objek berwarna yang jelas."
        else:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = result.names[cls_id]
                conf = float(box.conf[0])
                xyxy = box.xyxy[0].tolist()

                predictions.append({
                    "label": label,
                    "confidence": round(conf, 2),
                    "box": [round(coord, 2) for coord in xyxy]
                })

    # Jika tidak ada prediksi dengan confidence yang cukup tinggi
    if not predictions and not validation_message:
        validation_message = "Warna terdeteksi namun tingkat kepercayaan terlalu rendah. Coba gunakan gambar dengan pencahayaan yang lebih baik."

    # Simpan hasil deteksi ke file
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], "output.jpg")
    results[0].save(filename=result_path)

    return render_template("index.html", 
                         predictions=predictions, 
                         output_image="output.jpg",
                         validation_message=validation_message)
   
if __name__ == "__main__":
    app.run(debug=True)

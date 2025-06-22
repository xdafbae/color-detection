🖼️ Color Detection with YOLOv8 by Dafa Yudistira
Deteksi warna otomatis berbasis Computer Vision menggunakan model YOLOv8 yang dilatih dari dataset Roboflow. Proyek ini memungkinkan pengguna mengunggah gambar dan mendeteksi warna-warna seperti red, yellow, green, blue, dll secara instan melalui antarmuka web sederhana (Flask).

📌 Fitur Utama
🔍 Deteksi warna objek secara real-time menggunakan YOLOv8

🌐 Antarmuka web berbasis Flask untuk upload dan visualisasi hasil

🧠 Model dilatih menggunakan dataset anotasi warna dari Roboflow

💾 Hasil prediksi ditampilkan secara visual dan dalam bentuk confidence score

📂 Dataset
Proyek ini menggunakan dataset dari Roboflow versi 3:

🔗 Dataset Link:
Color Classification Dataset (Roboflow)

🛠️ Kebutuhan Sistem
Python 3.8+

Paket Python:

ultralytics

flask

roboflow

opencv-python

pillow

matplotlib

🚀 Cara Menjalankan
Clone Repository



git clone https://github.com/<your-username>/color-detection.git
cd color-detection
Install Dependency


Salin
Edit
pip install -r requirements.txt
Jalankan Web App



python app.py
Buka Browser


http://localhost:5000

🧠 Pelatihan Model (Training)
Jika ingin melakukan pelatihan ulang:

python

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("u-long-kfqut").project("color-uuncb")
dataset = project.version(3).download("yolov8")
Lalu latih dengan:

python
Salin
Edit
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="Color-3/data.yaml", epochs=10, imgsz=416)
📁 Struktur Folder
php
Salin
Edit
color-detection/
├── app.py               # Aplikasi web Flask
├── templates/
│   └── index.html       # Halaman upload & hasil deteksi
├── static/
│   └── output.jpg       # Gambar hasil deteksi
├── color-detector/      # Folder model hasil training (ignored in .gitignore)
├── Color-3/             # Dataset lokal (ignored in .gitignore)
└── requirements.txt     # Daftar dependensi
👤 Author
Dafa Yudistira
Email: dafayudistira24@gmail.com
Project for Computer Vision Implementation

Kalau kamu ingin versi bahasa Indonesia, badge GitHub, atau README yang ada preview hasil deteksi (GIF/PNG), tinggal bilang, saya bantu buatkan.

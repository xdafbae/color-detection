from roboflow import Roboflow
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt


# Ganti API key jika kamu punya sendiri
rf = Roboflow(api_key="cVpz41AJvfaQWKOwXJLn")  
project = rf.workspace("u-long-kfqut").project("color-uuncb")
version = project.version(3)

# Download dalam format YOLOv8 
dataset = version.download("yolov8")

# Load model YOLOv8 nano (ringan)
model = YOLO("yolov8n.pt")

# Train model dengan dataset dari Roboflow
model.train(
    data=dataset.location + "/data.yaml",   # path ke data.yaml
    epochs=10,                              # jumlah epoch
    imgsz=416,                              # resolusi gambar
    batch=8,                               # ukuran batch
    project="color-detector",               # nama folder proyek
    name="yolov8-color-v3",                 # nama eksperimen
    verbose=True
)

model = YOLO("color-detector/yolov8-color-v32/weights/best.pt")

# Path gambar yang ingin diuji
test_image_path = "/content/Color-3/valid/images/original-17070-1452705661-16_webp.rf.feab19ed2d174843ed30c1f9ee6a5d32.jpg"  # ← Ganti dengan gambar kamu

# Lakukan deteksi objek warna
results = model(test_image_path, save=True, show=True)  # save hasil & tampilkan window

# img = cv2.imread(test_image_path)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Tampilkan gambar asli
# plt.figure(figsize=(8, 6))
# plt.imshow(img_rgb)
# plt.axis('off')
# plt.title("Gambar Input")
# plt.show()

# # Cetak hasil deteksi
# for result in results:
#     for box in result.boxes:
#         cls_id = int(box.cls[0])
#         label = result.names[cls_id]
#         conf = float(box.conf[0])
#         xyxy = box.xyxy[0].tolist()

#         print(f"Label Warna : {label}")
#         print(f"Confidence   : {conf:.2f}")
#         print(f"Koordinat Box: {xyxy}")
#         print("-" * 40)

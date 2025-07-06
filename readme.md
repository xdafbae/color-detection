## 🖼️ Color Detection
Automatic color detection using Computer Vision powered by a YOLOv8 model trained on a Roboflow dataset. This project allows users to upload images and instantly detect colors such as red, yellow, green, blue, etc., through a simple web interface built with Flask.

## 🧠 Background
Color detection is one of the fundamental techniques in digital image processing, widely used in the field of Computer Vision. Color can serve as a visual cue to recognize and distinguish objects in an image. This technique has various applications, such as object tracking, product classification, and surveillance systems. By utilizing color representations like RGB or HSV, computers can automatically detect and process objects based on color.

## 📌 Main Features
- 🔍 Object color detection using YOLOv8

- 🌐 Web interface built with Flask for image upload and result visualization

- 🧠 Model trained using a color-annotated dataset from Roboflow

- 💾 Prediction results displayed visually with bounding boxes and confidence scores

- 📂 Dataset
This project uses a color classification dataset from Roboflow (version 3).

## 🔗 Dataset Link:
Color Classification Dataset (Roboflow)

🛠️ System Requirements
Input Image:

Digital images containing objects with distinct or contrasting colors.

Supported formats: JPG, PNG

🚀 Implementation Process
Image Input

Image is uploaded from the user as input data for processing.

Color Detection

The model detects color regions (e.g., red, yellow, green, etc.) and produces:

Color label

Confidence score

Bounding box coordinates

Display Results

Results are shown to the user in the form of:

Image with bounding boxes

Labels + confidence scores below the image

👤 Author
Dafa Yudistira

Email: dafayudistira24@gmail.com
Project for Computer Vision Implementation


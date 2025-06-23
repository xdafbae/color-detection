## 🖼️ Color Detection 
Deteksi warna otomatis berbasis Computer Vision menggunakan model YOLOv8 yang dilatih dari dataset Roboflow. Proyek ini memungkinkan pengguna mengunggah gambar dan mendeteksi warna-warna seperti red, yellow, green, blue, dll secara instan melalui antarmuka web sederhana (Flask).

## 🧠Latar Belakang 

Deteksi warna merupakan salah satu teknik dasar dalam pengolahan citra digital yang banyak digunakan dalam bidang Computer Vision. Warna dapat menjadi petunjuk visual untuk mengenali dan membedakan objek dalam sebuah gambar. Teknik ini memiliki berbagai aplikasi, seperti pelacakan objek, klasifikasi barang, dan sistem pengawasan. Dengan memanfaatkan representasi warna seperti RGB atau HSV, komputer dapat mendeteksi dan mengolah objek berdasarkan warna secara otomatis.

## 📌 Fitur Utama

- **🔍Deteksi warna objek secara real-time menggunakan YOLOv8
- **🌐 Antarmuka web berbasis Flask untuk upload dan visualisasi hasil
- **🧠 Model dilatih menggunakan dataset anotasi warna dari Roboflow
- **💾 Hasil prediksi ditampilkan secara visual dan dalam bentuk confidence score

##📂 Dataset

##Proyek ini menggunakan dataset dari Roboflow versi 3:

##🔗 Dataset Link:

- **Color Classification Dataset (Roboflow)

## 🛠️ Kebutuhan Sistem
- **Gambar sebagai Input : 
- **Gambar digital dengan objek yang memiliki warna mencolok atau kontras.
Bisa berupa file JPG, PNG,).

## Dataset Warna
- **https://universe.roboflow.com/u-long-kfqut/color-uuncb


## 🚀  Proses Implementasi
- **1.Inputan Gambar
- ** Gambar diambil dari file sebagai data yang akan di proses.

##2.Deteksi Warna
- ** Model mengenali area warna (seperti red, yellow, green, dll) dan menghasilkan:
- **Label warna,
- **Confidence score,
- **Koordinat bounding box,

## 3.Menampilkan Hasil
- ** Hasil ditampilkan ke pengguna dalam bentuk:
- **Gambar dengan bounding box warna
- **Label + confidence di bawah gambar



##👤 Author
Dafa Yudistira
Email: dafayudistira24@gmail.com
Project for Computer Vision Implementation



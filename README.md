# 🪖 Helmet Detection System (Image + Video | YOLOv8 + Flask)

A simple **Flask-based web application** that detects helmets in images and videos using **YOLO (Ultralytics)** and **OpenCV**.  

Users can upload images or videos, and the app will detect whether people are wearing helmets, marking the results visually.

---

## 🌟 Features

- Detects **with helmet** and **without helmet** in images and videos
- Supports multiple formats:
  - **Images:** PNG, JPG, JPEG  
  - **Videos:** MP4, AVI, MOV  
- Automatically draws **bounding boxes** on detected objects
- Stores uploaded files temporarily in `static/uploads/`  
- Easy deployment to **Render, Railway, or PythonAnywhere**

---

## 📁 Project Structure

helmet-detection/
├── app.py          
├── model.py        
├── best.pt         
├── requirements.txt
├── templates/
│   └── index.html  
├── static/
│   └── uploads/    

## Quick Install

1. Clone repo and enter folder: `git clone https://github.com/rafay-datascientistAI/6-Real-Time-Helmet-Detection-API.git`  
2. Create virtual environment and activate: `python -m venv venv && source venv/bin/activate` (Windows: `.\venv\Scripts\activate`)  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run app: `python app.py` and open `http://127.0.0.1:5000` in browser

## 📸 How It Works

- Upload an image or video through the interface  
- The YOLOv8 model processes the input  
- Helmet detection is performed frame-by-frame (for video)  
- Output is displayed with bounding boxes and labels  

## 🧠 Tech Stack

Python • YOLOv8 • Flask • OpenCV • PyTorch • HTML

## 🔌 API Usage

**Endpoint:** POST /predict  

**Input:**  
- Image file  
- Video file  

**Output:**  
- Processed image or video with detections  
- JSON response (optional)

## 🎯 Use Cases

- Workplace safety monitoring  
- Traffic surveillance  
- Smart AI applications  

## 👨‍💻 Author

Muhammad Rafay  

GitHub: https://github.com/rafay-datascientistAI  
LinkedIn: https://www.linkedin.com/in/muhammad-rafay-30267b3b7/

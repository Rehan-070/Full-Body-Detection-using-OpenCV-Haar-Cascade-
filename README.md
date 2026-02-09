# 🧍 Full Body Detection using OpenCV (Haar Cascade)

A real-time full body detection program using OpenCV and Haar Cascade classifier. The application captures live video from a webcam and detects human bodies by drawing bounding boxes.

---

## 🚀 Features

- 🎥 Real-time webcam video processing
- 🧍 Full body detection using Haar Cascade
- 🟩 Green bounding box around detected bodies
- ⌨️ Press `a` to stop the camera
- ⚡ Lightweight and fast detection

---

## 🧠 How It Works

1. Haar Cascade full body classifier is loaded
2. Webcam captures live video frames
3. Frames are converted to grayscale
4. Full bodies are detected using `detectMultiScale`
5. Rectangles are drawn around detected bodies

---

## 🗂️ Project Files

main.py  

Main file contains OpenCV logic for live detection.

---

## 🛠️ Requirements

Make sure you have **Python 3.x** installed.

Install required library using:

`pip install opencv-python`

---

## ▶️ How to Run

# main file  
`main.py`

# run the program  
`python main.py`

Make sure the Haar Cascade file path is correct:

`haarcascade_fullbody.xml`

---

## 🧪 Example Output

- Webcam window opens
- Human bodies are detected
- Green rectangles appear on detected bodies
- Press **a** to exit the program

---

## 📚 Libraries Used

`opencv-python` - Computer vision & image processing  

---

## 🤝 Contributing

- Fork the repository
- Improve features like:
  - Face + body detection
  - Detection accuracy tuning
  - FPS counter
  - Video file input support
- Create a pull request

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## Author

Rehan Shaikh

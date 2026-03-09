# AI-Based Industrial Defect Detection System

## Project Overview

The **AI-Based Industrial Defect Detection System** is a machine learning project designed to automatically detect defects in industrial products using computer vision techniques. The system analyzes images of industrial surfaces and identifies whether a product is **defective or non-defective**.

This project uses a trained deep learning model to help improve **quality control in manufacturing industries** by reducing manual inspection time and increasing detection accuracy.

---

## Objectives

* Automate the process of industrial defect detection.
* Reduce human error in quality inspection.
* Provide a simple web interface for testing images.
* Demonstrate the use of AI in real-world manufacturing applications.

---

## Features

* Upload industrial surface images.
* Detect defects using a trained AI model.
* Display prediction results instantly.
* Simple and interactive web interface built with Streamlit.

---

## Technologies Used

* Python
* Streamlit
* YOLO (You Only Look Once) Object Detection
* Ultralytics
* OpenCV
* NumPy

---

## Project Structure

```
AI_Industrial_Defect_Detection
│
├── app.py              # Streamlit web application
├── best.pt             # Trained YOLO model weights
├── test.jpg            # Sample test image
├── dataset/            # Training dataset (optional)
└── README.md           # Project documentation
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/AI_Industrial_Defect_Detection.git
```

2. Navigate to the project folder

```
cd AI_Industrial_Defect_Detection
```

3. Install required libraries

```
pip install -r requirements.txt
```

---

## How to Run the Project

Run the Streamlit application:

```
python -m streamlit run app.py
```

After running the command, open the following link in your browser:

```
http://localhost:8501
```

Upload an image to check whether the product contains defects.

---

## Applications

* Manufacturing quality control
* Automated inspection systems
* Smart factories
* Industrial production monitoring

---

## Future Improvements

* Real-time defect detection using cameras
* Integration with industrial monitoring systems
* Dashboard for defect statistics and analytics
* Support for multiple defect types

---

## Author

**Alishba Riaz**

---

## License

This project is for educational and research purposes.

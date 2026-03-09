import streamlit as st
from PIL import Image
import numpy as np
import cv2
from ultralytics import YOLO
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
import tempfile

# --- 1. Page Config ---
st.set_page_config(page_title="AI Industrial Defect Detection", layout="wide", page_icon="🏭")

# --- 2. Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    section[data-testid="stSidebar"] { background-color: #1e3a8a !important; border-right: 2px solid #000; }
    section[data-testid="stSidebar"] * { color: #ffffff !important; font-weight: 700 !important; }
    .main-header { text-align: center; padding: 30px; background-color: #ffffff; border-radius: 15px; border-bottom: 6px solid #1e3a8a; margin-bottom: 30px; }
    .main-header h1 { color: #1e3a8a; font-size: 40px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Model Loading with Error Catching ---
@st.cache_resource
def load_yolo_model():
    try:
        model = YOLO("best.pt")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_yolo_model()
LOG_FILE = "industrial_logs.csv"

# --- 4. Sidebar ---
with st.sidebar:
    st.markdown("## ⚙️ DASHBOARD MENU")
    app_mode = st.selectbox("CHOOSE VIEW:", ["Live Inspection", "Analytics Report"])
    # Yahan sensitivity kam kar ke check karein
    conf_level = st.slider("AI SENSITIVITY (Lower if no defects found):", 0.05, 1.0, 0.25)
    st.success("SYSTEM ONLINE ✅")

# --- 5. Main Content ---
if app_mode == "Live Inspection":
    st.markdown('<div class="main-header"><h1>AI INDUSTRIAL DEFECT DETECTION</h1></div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.tabs(["📸 Static Image", "📹 Video File", "📡 Live Camera"])

    with t1:
        img_file = st.file_uploader("Upload Inspection Photo", type=['jpg','png','jpeg'])
        if img_file:
            img = Image.open(img_file)
            
            # --- DEBUGGING START ---
            results = model.predict(source=img, conf=conf_level)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.image(results[0].plot(), caption="Detection Result", use_container_width=True)
            
            with col2:
                st.markdown("### 📋 AI Diagnosis")
                boxes = results[0].boxes
                if len(boxes) > 0:
                    st.warning(f"Detected {len(boxes)} potential issues")
                    for box in boxes:
                        label = model.names[int(box.cls[0])]
                        conf = float(box.conf[0])
                        st.write(f"📍 **{label}** - Confidence: {conf:.2f}")
                else:
                    st.info("No defects detected with current sensitivity.")
                    # Is se terminal mein detail nazar aayegi
                    print("Debug: AI did not find any objects above the threshold.")
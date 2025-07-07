import streamlit as st

def show():
    st.title("📖 About Us")

    st.markdown("""
    # 👥 About Us
    ### Research Behind the Deepfake Detection System

    ---

    ## 🧠 Project Vision

    The growing prevalence of synthetic media poses a significant threat to the authenticity of digital information. Our research-based project is focused on the **automated detection of deepfakes** in videos using machine learning and computer vision techniques. By leveraging the **FaceForensics++ dataset** and deep convolutional architectures, we aim to contribute to the ongoing efforts in securing digital media and combating misinformation.

    ---

    ## 🛠️ What We Built

    This project centers around a **binary classification model** trained to differentiate between real and manipulated facial footage. Using a lightweight yet powerful **Xception CNN architecture**, we ensure both performance and accuracy are optimized. We preprocess video frames by detecting and extracting facial regions using **Dlib**, and apply consistent training-time transformations to maintain inference reliability.

    Key Components:
    - 📁 Preprocessed FaceForensics++ (C23)
    - 🧠 Xception-based CNN
    - 📉 BCEWithLogitsLoss for binary classification
    - 📊 Majority voting across video frames
    - 🎞️ Streamlit interface for easy testing

    ---

    ## 🔬 Research Objectives

    - Build a lightweight and accurate deepfake detection model
    - Ensure alignment between training (face-based) and testing pipelines
    - Evaluate on compressed real-world data
    - Support video-level prediction with confidence outputs
    - Enable practical and user-friendly detection via Streamlit

    ---
    ---
    """)

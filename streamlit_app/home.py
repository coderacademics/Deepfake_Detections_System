import streamlit as st

def show():
    image = "home_bg.jpg"
    st.image(image,use_container_width=True)
    st.markdown("""
    # 🎭 Deepfake Detection System
    ### Robust Detection of Synthetic Media Using FaceForensics++ and Deep Learning

    ---

    ## 🔍 About the Project

    With the rapid advancement of generative models, deepfakes have become increasingly realistic and potentially harmful. This research-driven project addresses the growing concern of deepfake videos by building a robust detection pipeline using a custom-trained Convolutional Neural Network (CNN) based on the **Xception architecture**.

    We leverage the **FaceForensics++ dataset (C23 compressed)** and extract face regions from video frames to train and evaluate a model capable of distinguishing between **real** and **manipulated** videos with high accuracy.

    ---

    ## 🚀 Key Features

    - 🧠 **Model**: Custom Xception CNN trained on face-cropped frames
    - 📦 **Dataset**: FaceForensics++ (Real, Deepfakes, Face2Face, FaceSwap, etc.)
    - 🎞️ **Video Inference**: Frame-level prediction with majority voting
    - 🔍 **Face Detection**: Dlib-based cropped face alignment (1.5× bounding box padding)
    - 📈 **Accuracy**: Achieved >95% accuracy on test and validation sets
    - 🛡️ **Binary Classification**: `Real (1)` vs `Fake (0)` using sigmoid thresholding
    - 🧪 **Live Testing**: Upload and test any video for deepfake classification

    ---

    ## 🧪 How It Works

    1. 👤 **Face Extraction**  
    We use Dlib’s frontal face detector to crop and align face regions from each video frame with slight padding.

    2. 🧠 **CNN-based Classification**  
    Each frame is passed through the trained Xception model to get a `Real` or `Fake` probability.

    3. 🧮 **Majority Voting**  
    After scanning multiple frames, the system classifies the entire video based on the majority prediction.

    ---

    ## 📁 Dataset Summary

    - 📂 **Train Set**: 29,000 frames  
    - 📂 **Validation Set**: 6,300 frames  
    - 📂 **Test Set**: 6,300 frames  
    - 💾 Format: JPEG images extracted at regular intervals from compressed `.mp4` videos

    ---

    ## 🎯 Use Cases

    - ✅ Content Verification for Social Media
    - 🎥 Forensics in Law Enforcement
    - 🧪 Academic Research in Media Security
    - 🛡️ Anti-Misinformation Tools

    ---

    ## 👨‍💻 Authors & Research

    This project is part of a research initiative in deepfake detection using vision-based models and real-world benchmark datasets.

    *For more technical details, refer to the "About Us" page or test your own videos in the "Test Video" section.*

    ---
    """)

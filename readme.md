# 🧠 Deepfake Detection System from Videos

A complete deep learning-based application to detect **deepfake videos** using a fine-tuned `Xception` model trained on the **FaceForensics++ C23 dataset**. Built using **PyTorch** and **Streamlit**, this project allows you to upload and analyze `.mp4` videos in real-time, and classify them as **Real** or **Fake** based on face frame analysis.

---

## 📌 Features

- 🔍 Detect deepfakes in uploaded videos using a trained binary classifier
- 🎯 Model trained on **FaceForensics++** with high accuracy:  
  - ✅ Train Accuracy: **99.2%**  
  - 🧪 Validation Accuracy: **95.3%**  
  - 📊 Test Accuracy: **95.42%**
- 🤖 Face detection with `dlib` + 1.5x padding
- 📼 Frame-wise inference using a custom CNN (`Xception`)
- 📁 Multi-page Streamlit App (Home, About Us, Check DeepFake)
- 💾 Lightweight UI for local video upload and inference

---

## 🗂️ Project Structure

```

deepfake-detection/
├── main.py                      # Entry point - Streamlit router
├── home.py                      # Home page content
├── aboutus.py                   # About Us page
├── check\_deepfake.py            # Deepfake detection logic + UI
├── xception\_faceforensics\_final.pt  # Trained model weights
├── README.md
└── requirements.txt

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/deepfake-detection.git
cd deepfake-detection
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the trained model

Place your trained model file (`xception_faceforensics_final.pt`) inside the project root directory.

> ⚠️ If you don’t have the model file, contact the author or retrain the model using the FaceForensics++ dataset.

### 4. Run the Streamlit app

```bash
streamlit run main.py
```

---

## 📽️ How to Use

1. Launch the Streamlit app.
2. Navigate to **"Check DeepFake"** from the sidebar.
3. Upload a `.mp4` video file.
4. Click **"Run Detection"**.
5. The app will:

   * Extract faces from video frames
   * Run inference using the trained Xception model
   * Display a prediction result (Real/Fake)
   * Show percentage confidence based on frame votes

---

## 🧠 Model Details

* **Architecture:** `Xception` (via `timm`)
* **Input:** 256x256 RGB cropped face frames
* **Output:** Binary classification (Real = 1, Fake = 0)
* **Dataset:** FaceForensics++ C23
* **Loss Function:** `BCEWithLogitsLoss`
* **Optimizer:** `Adam` with learning rate = 0.0001
* **Frame Sampling:** Every 30th frame

---

## 📊 Results

| Metric         | Value  |
| -------------- | ------ |
| Train Accuracy | 99.2%  |
| Val Accuracy   | 95.3%  |
| Test Accuracy  | 95.42% |

---

## 🖼️ Example Result

```
Video: user_upload.mp4
Result: 🔴 FAKE
Real frames: 12.8%
Fake frames: 87.2%
```

---

## 👨‍💻 Author

**Saikat Mohanta**
🔗 [LinkedIn](https://www.linkedin.com/in/saikat-mohanta43434/)
🐙 [GitHub](https://github.com/saikat-mohanta)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌱 Future Scope

* 🎥 Real-time webcam-based deepfake detection
* 📤 Batch video processing + report export
* ☁️ Deploy using Hugging Face Spaces or Streamlit Cloud
* 📈 Add Grad-CAM visualization for explainability

---

## 🙌 Acknowledgements

* [FaceForensics++ Dataset](https://github.com/ondyari/FaceForensics)
* [timm Models](https://github.com/huggingface/pytorch-image-models)
* [dlib Face Detector](http://dlib.net/)

---

```

---

Let me know if you also want:
- A `requirements.txt` file
- A `LICENSE` file (MIT or something else)
- A GitHub repository description and tags suggestion

I'm happy to help with that too!
```

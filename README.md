# Skin Disease Classification and Severity Analysis

AI-powered web application for **skin disease classification and severity analysis** using deep learning and clustering techniques.

---

## 🌐 Live Demo

**Deployed Application:**
https://skin-disease-classification-and-severity.onrender.com/

Upload a skin image to receive:

* Disease classification
* Severity stage prediction
* Confidence score
* Suggested next steps

---

## 📌 Project Overview

This project is a **web-based AI system** designed to analyze skin lesion images and predict:

1. **Skin Disease Class** using a trained **Convolutional Neural Network (CNN)**
2. **Severity Stage** using **PCA + KMeans clustering** applied to extracted CNN features

The application combines **deep learning for image classification** with **unsupervised learning for severity estimation**.

The system consists of:

* **Frontend:** Static HTML/CSS/JavaScript interface for image upload and results display
* **Backend:** FastAPI server handling prediction requests
* **Machine Learning Models:** CNN classifier + PCA + KMeans severity model

---

## ✨ Features

* Drag-and-drop **image upload interface**
* AI-powered **skin disease classification**
* **Severity prediction**: Early, Moderate, Severe
* Confidence score visualization
* REST API powered by **FastAPI**
* Automatic **model health monitoring endpoint**
* Cloud deployment for public access

---

## 🧠 Machine Learning Pipeline

The prediction workflow follows these steps:

1. User uploads a skin lesion image
2. Image is sent to the FastAPI backend
3. Image is preprocessed and resized
4. CNN model predicts the **disease class**
5. CNN feature extractor generates embeddings
6. **PCA** reduces the feature dimensions
7. **KMeans clustering** predicts the severity stage
8. Backend returns disease, severity, confidence, and suggestion
9. Frontend displays the results

---

## 🏗 System Architecture

```
Frontend (HTML / CSS / JavaScript)
            │
            ▼
      FastAPI Backend
            │
            ▼
      CNN Model (TensorFlow)
            │
            ▼
   Feature Extraction Layer
            │
            ▼
        PCA Model
            │
            ▼
      KMeans Clustering
            │
            ▼
        Prediction API
```

---

## 📂 Project Structure

```
.
|-- api/
|   |-- main.py
|   |-- predictor.py
|   |-- config.py
|   `-- requirements.txt
|
|-- frontend/
|   |-- index.html
|   |-- script.js
|   `-- style.css
|
|-- models/
|   |-- best_cnn_model.h5
|   |-- label_encoder.pkl
|   |-- pca_model.pkl
|   `-- kmeans_severity.pkl
|
|-- run-new.bat
`-- README.md
```

---

## ⚙️ Tech Stack

### Backend

* Python
* FastAPI
* TensorFlow / Keras
* scikit-learn
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

### Machine Learning

* CNN for disease classification
* PCA for dimensionality reduction
* KMeans for severity clustering

### Deployment

* Cloud deployment via Render

---

## 💻 Requirements

* Windows / Linux / macOS
* Python 3.10+
* Internet connection for dependency installation

If TensorFlow installation fails on Windows, install:

https://aka.ms/vs/17/release/vc_redist.x64.exe

---

## 🚀 Running the Project Locally

### Option 1 — One-click launcher

Run:

```
cd "D:\SKIN DISEASE C AND S GIT"
.\run-new.bat
```

This script will:

* create or activate `venv`
* install dependencies
* start the FastAPI server
* open the frontend page

---

### Option 2 — Manual Run

Start backend:

```
cd "D:\SKIN DISEASE C AND S GIT"
.\venv\Scripts\python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Open frontend:

```
start .\frontend\index.html
```

---

## 🔌 API Endpoints

Root

```
http://127.0.0.1:8000/
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Health Check

```
http://127.0.0.1:8000/health
```

Prediction Endpoint

```
POST /predict
```

---

## 🧪 Health Check Example

```
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content
```

Expected response:

```
{"status":"ok","model_loaded":true,"error":null}
```

---

## 📊 Example API Response

```
{
  "disease": "Melanoma",
  "severity": "Moderate Stage",
  "confidence": 0.9132,
  "suggestion": "Dermatological consultation recommended for proper examination."
}
```

---

## 📝 Notes

* Pre-trained models are stored in the `models/` directory
* Model loading is verified during server startup
* The frontend is static and does not require a build step
* Designed primarily for educational and research purposes

---

## 📤 Git Commands

To push the project to GitHub:

```
cd "D:\SKIN DISEASE C AND S GIT"
git remote set-url origin https://github.com/gramya125/Skin-disease-classification-and-Severity-analysis.git
git push -u origin main
```

---

## ⚠️ Disclaimer

This application is **not a medical device** and should not be used as a substitute for professional diagnosis or treatment.

Always consult a **qualified dermatologist or medical professional** for medical advice.

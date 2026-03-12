# Skin Disease Classification and Severity Analysis

This project is a skin image analysis web app with a FastAPI backend and a static frontend. It predicts:

- Skin disease class using a trained CNN model
- Severity stage using PCA + KMeans on extracted CNN features

The app is designed for local use on Windows and includes pre-trained model files inside the `models/` folder.

## Project Structure

```text
.
|-- api/
|   |-- main.py
|   |-- predictor.py
|   |-- config.py
|   `-- requirements.txt
|-- frontend/
|   |-- index.html
|   |-- script.js
|   `-- style.css
|-- models/
|   |-- best_cnn_model.h5
|   |-- label_encoder.pkl
|   |-- pca_model.pkl
|   `-- kmeans_severity.pkl
|-- run-new.bat
`-- README.md
```

## Features

- Image upload with drag and drop UI
- Disease prediction from skin lesion image
- Severity prediction as Early, Moderate, or Severe stage
- Confidence score display
- FastAPI `/docs` interface for backend testing
- `/health` endpoint to confirm model loading

## Tech Stack

- Python
- FastAPI
- TensorFlow / Keras
- scikit-learn
- HTML, CSS, JavaScript

## Requirements

- Windows
- Python 3.10 or newer
- Internet connection for first-time dependency install

If TensorFlow installation fails on Windows, install the Visual C++ Redistributable:

`https://aka.ms/vs/17/release/vc_redist.x64.exe`

## How to Run

### Option 1: One-click launcher

Run:

```powershell
cd "D:\SKIN DISEASE C AND S GIT"
.\run-new.bat
```

This script:

- creates or uses `venv/`
- installs dependencies
- starts the backend server
- opens the frontend page

### Option 2: Manual run

Start the backend:

```powershell
cd "D:\SKIN DISEASE C AND S GIT"
.\venv\Scripts\python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Open the frontend:

```powershell
start .\frontend\index.html
```

## API Endpoints

- Root: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`
- Prediction endpoint: `POST /predict`

Health check example:

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content
```

Expected response:

```json
{"status":"ok","model_loaded":true,"error":null}
```

## Prediction Flow

1. User uploads a skin image from the frontend
2. Frontend sends the image to the FastAPI backend
3. CNN model predicts the disease class
4. Feature extractor generates embeddings from the CNN
5. PCA reduces the feature dimensions
6. KMeans predicts severity stage
7. Backend returns disease, severity, confidence, and suggestion

## Output Format

Example API response:

```json
{
  "disease": "Melanoma",
  "severity": "Moderate Stage",
  "confidence": 0.9132,
  "suggestion": "Dermatological consultation recommended for proper examination."
}
```

## Notes

- The project uses pre-trained local model files from the `models/` folder.
- Model loading is checked at startup through the `/health` endpoint.
- The frontend is static and does not require a separate build step.
- This project is for educational and research purposes only.

## Git Commands

If you want to push this project to GitHub:

```powershell
cd "D:\SKIN DISEASE C AND S GIT"
git remote set-url origin https://github.com/gramya125/Skin-disease-classification-and-Severity-analysis.git
git push -u origin main
```

## Disclaimer

This application is not a medical device and should not be used as a substitute for professional diagnosis or treatment. Always consult a qualified dermatologist or medical professional.

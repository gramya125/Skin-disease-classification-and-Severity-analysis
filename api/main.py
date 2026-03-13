from contextlib import suppress

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io

try:
    from .config import (
        SEVERITY_MAP,
        DISEASE_MAP,
        SUGGESTION_MAP,
    )
    from .predictor import SkinPredictor
except ImportError:
    from config import (
        SEVERITY_MAP,
        DISEASE_MAP,
        SUGGESTION_MAP,
    )
    from predictor import SkinPredictor


app = FastAPI(title="Skin Disease Prediction API", version="2.0")


# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")


predictor = None
model_load_error = None


# Try loading model
with suppress(Exception):
    predictor = SkinPredictor()

if predictor is None:
    try:
        predictor = SkinPredictor()
    except Exception as exc:
        model_load_error = str(exc)


# Root endpoint → serve website
@app.get("/")
def root():
    return FileResponse("frontend/index.html")


# Health check
@app.get("/health")
def health():
    return {
        "status": "ok" if predictor is not None else "error",
        "model_loaded": predictor is not None,
        "error": model_load_error,
    }


# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if predictor is None:
        raise HTTPException(
            status_code=503,
            detail=f"Model not loaded: {model_load_error or 'unknown startup error'}",
        )

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    short_name, severity_id, confidence = predictor.predict(image)

    disease = DISEASE_MAP.get(short_name, short_name)
    severity = SEVERITY_MAP.get(severity_id, "Moderate Stage")

    suggestion = SUGGESTION_MAP.get(
        severity, "Consult a dermatologist for evaluation."
    )

    return {
        "disease": disease,
        "severity": severity,
        "confidence": round(confidence, 4),
        "suggestion": suggestion
    }

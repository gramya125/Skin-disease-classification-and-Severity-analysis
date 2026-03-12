from contextlib import suppress

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = None
model_load_error = None

with suppress(Exception):
    predictor = SkinPredictor()

if predictor is None:
    try:
        predictor = SkinPredictor()
    except Exception as exc:
        model_load_error = str(exc)


@app.get("/")
def root():
    return {"message": "Skin Disease Prediction API running. Use /docs to test."}


@app.get("/health")
def health():
    return {
        "status": "ok" if predictor is not None else "error",
        "model_loaded": predictor is not None,
        "error": model_load_error,
    }


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
        "confidence": round(confidence,4),
        "suggestion": suggestion
    }

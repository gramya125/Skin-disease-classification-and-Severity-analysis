from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATHS = {
    "cnn": MODELS_DIR / "best_cnn_model.h5",
    "le": MODELS_DIR / "label_encoder.pkl",
    "pca": MODELS_DIR / "pca_model.pkl",
    "kmeans": MODELS_DIR / "kmeans_severity.pkl",
}

SEVERITY_MAP = {
    0: "Early Stage",
    1: "Moderate Stage",
    2: "Severe Stage"
}

DISEASE_MAP = {
    "akiec": "Actinic Keratoses and Intraepithelial Carcinoma",
    "bcc": "Basal Cell Carcinoma",
    "bkl": "Benign Keratosis-like Lesions",
    "df": "Dermatofibroma",
    "mel": "Melanoma",
    "nv": "Melanocytic Nevi",
    "vasc": "Vascular Lesions"
}

# Suggestions based on severity only
SUGGESTION_MAP = {
    "Early Stage": "Monitor the lesion and maintain skin hygiene. Consult a dermatologist if changes appear.",
    "Moderate Stage": "Dermatological consultation recommended for proper examination.",
    "Severe Stage": "Immediate medical attention from a dermatologist is strongly recommended."
}

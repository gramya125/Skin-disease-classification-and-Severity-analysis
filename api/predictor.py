import numpy as np
import joblib
from tensorflow.keras.models import load_model, Model

try:
    from .config import MODEL_PATHS
except ImportError:
    from config import MODEL_PATHS


class SkinPredictor:

    def __init__(self):
        missing_files = [str(path) for path in MODEL_PATHS.values() if not path.exists()]
        if missing_files:
            raise FileNotFoundError(
                f"Missing model files: {', '.join(missing_files)}"
            )

        # Load CNN model
        self.cnn_model = load_model(str(MODEL_PATHS["cnn"]), compile=False)

        # Build model
        dummy = np.zeros((1,256,256,3))
        _ = self.cnn_model(dummy)

        # Feature extractor
        self.feature_extractor = Model(
            inputs=self.cnn_model.layers[0].input,
            outputs=self.cnn_model.layers[-2].output
        )

        # Load sklearn models
        self.le = joblib.load(MODEL_PATHS["le"])
        self.pca = joblib.load(MODEL_PATHS["pca"])
        self.kmeans = joblib.load(MODEL_PATHS["kmeans"])


    def preprocess(self, image):

        image = image.resize((256,256))
        image = np.array(image) / 255.0
        image = np.expand_dims(image,0).astype("float32")

        return image


    def predict(self, image):

        image = self.preprocess(image)

        # Disease prediction
        probs = self.cnn_model.predict(image, verbose=0)[0]
        class_id = np.argmax(probs)

        short_name = self.le.inverse_transform([class_id])[0]
        confidence = float(np.max(probs))

        # Severity prediction
        features = self.feature_extractor.predict(image, verbose=0)
        features_pca = self.pca.transform(features)

        severity_id = self.kmeans.predict(features_pca)[0]

        return short_name, severity_id, confidence

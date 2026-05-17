'''
*******************************
Author: u3327375, u3330354, u3334444
Group: Assignment 3
Assessment: Software Technology 1 (4483)
Date: 13/05/2026
*******************************
'''

from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import EDA_OUTPUT_DIR, MODEL_OUTPUT_DIR
from src.services.dataset_indexer import DatasetIndexer
from src.services.eda_service import EDAService
from src.services.image_preprocessor import ImagePreprocessor
from src.services.classifier_service import ClassifierService

class WorkflowService:
    """Coordinate the shared workflow for the project."""

    def __init__(self) -> None:
        EDA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        MODEL_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.indexer = DatasetIndexer()
        self.preprocessor = ImagePreprocessor()
        self.classifier = ClassifierService(self.preprocessor)
        self.dataframe = None

    def load_dataframe(self) -> pd.DataFrame:
        """Load and cache the indexed dataset."""
        if self.dataframe is None:
            print("Loading dataset...")
            self.dataframe = self.indexer.build_dataframe()
            print(f"Found {len(self.dataframe)} images across 17 species.")
        return self.dataframe

    def show_summary(self) -> None:
        """Build and print dataset summary statistics."""
        dataframe = self.load_dataframe()
        eda = EDAService(dataframe, EDA_OUTPUT_DIR)
        summary = eda.build_summary()
        print("\nDataset Summary:")
        print(f"  Total Images  : {summary['total_images']}")
        print(f"  Total Species : {summary['total_classes']}")
        print(f"  Avg Width     : {summary['mean_width']:.0f}px")
        print(f"  Avg Height    : {summary['mean_height']:.0f}px")

    def generate_eda(self) -> None:
        """Create and save the main EDA outputs."""
        dataframe = self.load_dataframe()
        eda = EDAService(dataframe, EDA_OUTPUT_DIR)
        print("\nGenerating EDA charts...")
        eda.save_class_distribution()
        eda.save_image_size_distribution()
        eda.save_sample_grid()
        print("Charts saved to outputs/eda/")

    def train_model(self) -> dict:
        """Train the baseline model, save it, and save evaluation outputs."""
        dataframe = self.load_dataframe()
        results = self.classifier.train(dataframe)
        self.classifier.save_model()

        # Save classification report
        report_path = MODEL_OUTPUT_DIR / "classification_report.txt"
        report_path.write_text(results["report"], encoding="utf-8")

        # Save confusion matrix
        plt.figure(figsize=(12, 10))
        sns.heatmap(
            results["confusion_matrix"],
            annot=False,
            cmap="Blues",
            xticklabels=results["labels"],
            yticklabels=results["labels"]
        )
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted Species")
        plt.ylabel("Actual Species")
        plt.tight_layout()
        plt.savefig(MODEL_OUTPUT_DIR / "confusion_matrix.png")
        plt.close()

        print(f"\nAccuracy: {results['accuracy']*100:.1f}%")
        print(f"Test images: 533")
        print(f"Results saved to outputs/models/")

        return results

    def predict_image(self, file_path: str) -> str:
        """Predict the class of one input image."""
        model_path = MODEL_OUTPUT_DIR / "macro_classifier.joblib"

        if not model_path.exists():
            raise FileNotFoundError("Train the model before running prediction.")

        self.classifier.model = joblib.load(model_path)
        features = self.preprocessor.transform(file_path).reshape(1, -1)
        prediction = self.classifier.model.predict(features)[0]

        if hasattr(self.classifier.model, "predict_proba"):
            probability = self.classifier.model.predict_proba(features).max()
            return f"{prediction} (Confidence: {probability:.1%})"

        return str(prediction)

    def run_full_pipeline(self) -> None:
        """Run the full Stage 1 and Stage 2 workflow."""
        self.show_summary()
        self.generate_eda()
        self.train_model()
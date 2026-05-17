'''
*******************************
Author: u3327375, u3330354, u3334444
Group: Assignment 3
Assessment: Software Technology 1 (4483)
Date: 13/05/2026
*******************************
'''

from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class EDAService:
    """Generate and save EDA outputs for the indexed image dataset."""

    def __init__(self, dataframe: pd.DataFrame, output_dir: Path) -> None:
        self.dataframe = dataframe
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_class_distribution(self) -> None:
        """Save a class-count chart for the dataset."""
        plt.figure(figsize=(12, 6))
        order = self.dataframe["label"].value_counts().index
        sns.countplot(data=self.dataframe, x="label", order=order)
        plt.xticks(rotation=90)
        plt.title("Macroinvertebrate Images per Class")
        plt.tight_layout()
        plt.savefig(self.output_dir / "class_distribution.png")
        plt.close()
        print("Saved class distribution chart.")

    def save_image_size_distribution(self) -> None:
        """Save width and height distribution charts."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        sns.histplot(self.dataframe["width"], bins=20, ax=axes[0])
        sns.histplot(self.dataframe["height"], bins=20, ax=axes[1])
        axes[0].set_title("Image Width Distribution")
        axes[1].set_title("Image Height Distribution")
        plt.tight_layout()
        plt.savefig(self.output_dir / "image_size_distribution.png")
        plt.close()
        print("Saved image size distribution chart.")

    def save_sample_grid(self, sample_count: int = 9) -> None:
        """Save a grid of sample images for quick visual inspection."""
        sample_df = self.dataframe.sample(min(sample_count, len(self.dataframe)), random_state=42)
        fig, axes = plt.subplots(3, 3, figsize=(10, 10))
        for ax, (_, row) in zip(axes.flat, sample_df.iterrows()):
            image = cv2.imread(row["file_path"])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            ax.imshow(image)
            ax.set_title(row["label"])
            ax.axis("off")
        for ax in axes.flat[len(sample_df):]:
            ax.axis("off")
        plt.tight_layout()
        plt.savefig(self.output_dir / "sample_grid.png")
        plt.close()
        print("Saved sample image grid.")

    def build_summary(self) -> dict:
        """Return key dataset summary statistics."""
        return {
            "total_images": int(len(self.dataframe)),
            "total_classes": int(self.dataframe["label"].nunique()),
            "mean_width": float(self.dataframe["width"].mean()),
            "mean_height": float(self.dataframe["height"].mean()),
        }
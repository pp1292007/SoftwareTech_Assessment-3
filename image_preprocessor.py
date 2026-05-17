'''
*******************************
Author: u3327375, u3330354, u3334444
Group: Assignment 3
Assessment: Software Technology 1 (4483)
Date: 13/05/2026
*******************************
'''

import cv2
import numpy as np
from src.config import IMAGE_SIZE

class ImagePreprocessor:
    """Convert raw images into model-ready numeric features."""

    def __init__(self, image_size: tuple = IMAGE_SIZE) -> None:
        self.image_size = image_size

    def transform(self, file_path: str) -> np.ndarray:
        """Load, resize, normalize, and flatten one image."""
        image = cv2.imread(str(file_path), cv2.IMREAD_GRAYSCALE)
        if image is None:
            return np.zeros(self.image_size[0] * self.image_size[1], dtype="float32")
        resized = cv2.resize(image, self.image_size)
        normalized = resized.astype("float32") / 255.0
        return normalized.flatten()
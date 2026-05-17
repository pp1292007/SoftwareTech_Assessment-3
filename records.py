'''
*******************************
Author: u3327375, u3330354, u3334444
Group: Assignment 3
Assessment: Software Technology 1 (4483)
Date: 13/05/2026
*******************************
'''

from dataclasses import dataclass
from pathlib import Path

@dataclass
class ImageRecord:
    """Store the core metadata for one indexed macroinvertebrate image."""
    file_path: Path
    label: str
    width: int
    height: int
    channels: int
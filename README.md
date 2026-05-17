# Macroinvertebrate Image Analysis System

## Group Members
- Member 1: u3327375
- Member 2: u3330354
- Member 3: u3334444

## Unit
Software Technology 1 (4483) — University of Canberra

## Project Goal
A Python application that loads 2,665 images of freshwater 
macroinvertebrates across 17 species, performs exploratory data 
analysis, and trains a classification model to identify species.

## Dataset
Kaggle Stream Macroinvertebrates
- 2,665 images across 17 species
- https://www.kaggle.com/datasets/kennethtm/stream-macroinvertebrates
- Place dataset inside: data/raw/stream_macroinvertebrates/

## Stages Completed
- Stage 1: Exploratory Data Analysis (EDA)
- Stage 2: Classification using Random Forest

## Features
- Loads and indexes 2,665 images from 17 species
- Generates 3 EDA charts saved to outputs/eda/
- Trains a Random Forest classifier with 71% accuracy
- Saves confusion matrix and classification report

## Libraries Used
- pandas
- numpy
- opencv-python
- matplotlib
- seaborn
- scikit-learn
- Pillow
- joblib

## How to Install
pip install -r requirements.txt

## How to Run
python -m src.main

## Project Structure
macro_project/
├── data/raw/stream_macroinvertebrates/
├── outputs/
│   ├── eda/
│   └── models/
├── src/
│   ├── config.py
│   ├── main.py
│   ├── models/records.py
│   └── services/
│       ├── dataset_indexer.py
│       ├── eda_service.py
│       ├── image_preprocessor.py
│       ├── classifier_service.py
│       └── workflow_service.py
├── requirements.txt
└── README.md

## Acknowledged Code
Code structure was adapted from the Assignment 3 Full Guidance 
and Coding Examples provided in the unit materials.
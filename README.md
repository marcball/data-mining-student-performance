# Student Performance Prediction – CSC 535 Final Project

This project was developed as part of a group assignment for CSC 535: Data Mining. The goal was to use machine learning techniques to predict student test scores based on socioeconomic and educational background factors.

We worked with a dataset containing information about students' gender, parental education, lunch status, and test preparation course, alongside their scores in math, reading, and writing.

## Project Objectives

- Predict individual and average test scores using various regression models
- Explore relationships between demographic features and performance
- Compare model performance using standard evaluation metrics
- Visualize results through graphs and charts

## Methods and Tools

- Language: Python
- Libraries: pandas, scikit-learn, matplotlib
- Models: Random Forest, Decision Tree, Neural Network (MLP)
- Dataset: StudentsPerformance.csv

Each model was trained on selected features and evaluated on math, reading, writing, and average scores.

## Process Overview

- Loaded and cleaned dataset using pandas
- Encoded categorical variables
- Added derived features (e.g., average score)
- Trained and tested each model using train/test split
- Evaluated model performance using Mean Squared Error and R²
- Visualized predictions against actual scores

## Installation

To install dependencies, run:

pip install -r requirements.txt

## Notes

This project was originally a collaborative effort. This version has been adapted for portfolio use, with names removed for privacy.
# Titanic Survival Prediction - Analytics Module

## Overview

This module focuses on building and evaluating machine learning models to predict passenger survival on the Titanic dataset. The workflow includes data preprocessing, model training, evaluation, handling class imbalance, hyperparameter tuning, regression analysis, and saving the best-performing model.

---

## Dataset

- Dataset: Titanic Dataset
- Source: Seaborn Dataset
- Saved locally as `titanic.csv`
- Target Variable: `survived`

### Features Used

- pclass
- sex
- age
- sibsp
- parch
- fare
- embarked

---

## Project Structure

```
analytics/
│
├── 01_eda.ipynb
├── 02_modeling.ipynb
├── titanic.csv
├── models/
│   └── best_pipeline.joblib
├── images/
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Joblib

---

## Workflow

### 1. Data Loading

- Loaded Titanic dataset from `titanic.csv`
- Selected relevant features and target variable
- Split data into training and testing sets using stratified sampling

---

### 2. Data Preprocessing

A preprocessing pipeline was created using `ColumnTransformer`.

#### Numerical Features

- Median Imputation
- Standard Scaling

#### Categorical Features

- Most Frequent Imputation
- One-Hot Encoding

---

### 3. Classification Models

The following machine learning models were trained:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Each model was implemented using Scikit-learn Pipelines.

---

### 4. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

The results were compared to identify the best-performing classifier.

---

### 5. Handling Class Imbalance

To improve classification performance on imbalanced data, the following techniques were applied:

- Logistic Regression with `class_weight="balanced"`
- SMOTE (Synthetic Minority Over-sampling Technique)

The performance of these approaches was compared with the baseline model.

---

### 6. Hyperparameter Tuning

Random Forest was optimized using GridSearchCV.

The following parameters were tuned:

- Number of Estimators
- Maximum Depth
- Maximum Features

The notebook displays:

- Best Parameters
- Best Cross-Validation Score
- Out-of-Bag (OOB) Score

---

### 7. Regression Analysis

A Linear Regression model was developed to predict passenger fare.

Regression metrics include:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Adjusted R² Score

A residual plot was also generated to evaluate model performance.

---

### 8. Model Persistence

The best classification model was saved using Joblib.

Saved model:

```
models/best_pipeline.joblib
```

The saved model was reloaded and tested to verify successful serialization.

---

## Outputs

The project generates:

- Trained classification models
- Model comparison table
- Confusion matrices
- ROC curves
- Decision tree visualization
- SMOTE comparison
- GridSearchCV results
- Regression metrics
- Residual plot
- Saved machine learning pipeline

---

## Conclusion

This project demonstrates a complete machine learning workflow using the Titanic dataset. It covers preprocessing, multiple classification algorithms, model evaluation, class imbalance handling, hyperparameter optimization, regression analysis, and model deployment through Joblib serialization. The modular pipeline design ensures reproducibility, scalability, and efficient model management.
# Predicting Term Deposit Subscription using Machine Learning

## Overview
This project aims to predict whether a customer will subscribe to a term deposit using machine learning techniques. The dataset used is the **Bank Marketing Dataset**, and we employ various classification algorithms, including **Logistic Regression, Decision Trees, Random Forest, and XGBoost**.

## Dataset
- **Source**: [Kaggle - Bank Marketing Dataset]
- **Features**:
  - Customer details: `age`, `job`, `marital`, `education`, `balance`, etc.
  - Contact details: `contact`, `day`, `duration`, `campaign`, `pdays`, etc.
  - Previous campaign outcomes: `previous`, `poutcome`
- **Target Variable**: `deposit` (Yes/No)

## Problem Statement
The goal is to build a predictive model that helps banks optimize their marketing strategies by identifying customers who are more likely to subscribe to a term deposit.

## Exploratory Data Analysis (EDA)
- Checked for missing values.
- Analyzed the distribution of the target variable (`deposit`).
- Identified correlations between features using a heatmap.
- Explored the impact of `duration`, `campaign`, and `poutcome` on `deposit`.

## Data Preprocessing
- Implemented a **Pipeline** for seamless data transformation.
- Used a **Preprocessor** to handle categorical and numerical features automatically.
- Scaled numerical features using **StandardScaler** within the pipeline.
- Addressed class imbalance using **SMOTE**.

## Model Training & Hyperparameter Tuning
We trained and evaluated multiple models:
1. **Logistic Regression**
2. **Decision Tree**
3. **Random Forest Classifier**
4. **XGBoost Classifier** (Best Model)

**Hyperparameter Tuning:**
- Used **GridSearchCV** for optimizing parameters like `max_depth`, `n_estimators`, and `learning_rate`.

## Model Evaluation
The trained XGBoost model was evaluated using multiple metrics:

- **Accuracy**
- **AUC Score**
- **Precision**
- **Recall**

The model performed well, achieving a high **AUC score**, which indicates strong predictive power. The **confusion matrix** showed a good balance between precision and recall.



## Key Insights
- **Duration** is the most influential factor in predicting deposit subscription.
- The XGBoost model performed best, making it ideal for deployment.
- Banks can use this model to focus marketing efforts on high-potential customers.

## Deployment
The trained XGBoost model has been deployed using **Flask**, making it accessible as a web application.

### **Project Structure**
- **`app.py`** – The Flask backend that handles model inference and API requests.
- **`templates/index.html`** – The frontend user interface for the web app.
- **`xgboost_pipeline.pkl`** -the model we created



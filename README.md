# 🚀 Machine Learning Projects

This repository contains various machine learning projects showcasing data preprocessing, model building, and deployment.

## 📌 Projects

### 1️⃣ [Term Deposit Subscription Prediction](Term%20deposit%20subscription/)
- **Goal:** Predict whether a customer will subscribe to a term deposit.
- **Dataset:** Bank Marketing Dataset (Source: [Kaggle](https://www.kaggle.com/))
- **Key Insights:**
  - Used **XGBoost Classifier** with **hyperparameter tuning**.
  - Evaluated using **Accuracy, Precision, Recall, and AUC Score**.
  - **Deployed using Flask** with a trained **XGBoost pipeline**.

### 2️⃣ [Automobile Price Prediction](Automobile%20Price%20Prediction/)
- **Goal:** Predict the price of an automobile based on various features.
- **Dataset:** Automobile Dataset (Source: [Kaggle](https://www.kaggle.com/))
- **Key Insights:**
  - Used **XGBoost Regressor** as the best-performing model.
  - Evaluated using **R² Score, Mean Squared Error (MSE), and Mean Absolute Error (MAE)**.
  - **Model saved as `xgb_model.pkl` for future predictions.**

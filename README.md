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

### 3️⃣ [Predicting Personal Loan Adoption with Machine Learning](Predicting%20Personal%20Loan%20Adoption%20with%20Machine%20Learning/)  
- **Goal:** Predict whether a customer will accept a personal loan based on financial and demographic factors.  
- **Dataset:** Personal Loan Dataset (Source: [Kaggle](https://www.kaggle.com/))  
- **Key Insights:**  
  - **Random Forest Classifier** performed best among tested models.  
  - Evaluated using **Accuracy, Precision, Recall, F1-Score, and AUC-ROC**.  
  - **Model saved as `random_forest_model.pkl` for future predictions.**  

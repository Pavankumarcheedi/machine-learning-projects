# Automobile Price Prediction

## 📌 Project Overview
This project focuses on predicting automobile prices using machine learning models. It involves data preprocessing, exploratory data analysis (EDA), and training regression models to make accurate price predictions.

## 📊 Dataset Source  
The dataset used in this project is sourced from **[Kaggle](https://www.kaggle.com/)**.  
Make sure to download the dataset from Kaggle and place it in the appropriate directory before running the notebook.

## 📂 Dataset
- **Dataset Used**: `cars.csv`
- The dataset contains various features such as engine size, horsepower, fuel type, and other vehicle attributes that influence price.

## 🛠️ Steps Involved
1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling
2. **Exploratory Data Analysis (EDA)**
   - Visualizing distributions and relationships between variables
3. **Model Training & Evaluation**
   - Trained models:
     - ✅ XGBoost Regressor
     - ✅ Random Forest Regressor
     - ✅ Linear Regression
   - Evaluation metrics:
     - 📊 R² Score
     - 📉 Mean Squared Error (MSE)
     - 📈 Mean Absolute Error (MAE)

## 📈 Results & Insights
- The models were evaluated based on performance metrics.


## 🏁 Conclusion
This project demonstrates the power of machine learning in predicting car prices with high accuracy. The trained models can assist dealerships and consumers in estimating fair market prices for vehicles.

## 🏆 Trained Model  
- The best-performing model was **XGBoost Regressor**.  
- The trained model is saved as a `.pkl` file for deployment.  
- Model file: `xgb_model.pkl`

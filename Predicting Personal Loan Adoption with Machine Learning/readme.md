# 📌 Predicting Personal Loan Adoption Using Machine Learning

## 📖 Project Overview
This project aims to predict whether a customer will accept a **personal loan** based on their financial and demographic attributes. Using **Machine Learning models** such as **Logistic Regression, Decision Trees, and Random Forest**, we analyze customer data to optimize **targeted marketing strategies** for banks and financial institutions.

## 📂 Dataset
- **Dataset Source** : [Kaggle](https://www.kaggle.com/)
The dataset includes various customer attributes:
- **Age**: Customer's age
- **Experience**: Years of professional experience
- **Income**: Annual income in thousands
- **ZIP Code**: Customer's residential area
- **Family**: Number of family members
- **CCAvg**: Average credit card spending per month
- **Education**: Customer's education level
- **Mortgage**: Mortgage loan value
- **Securities Account**: Whether the customer has a securities account
- **CD Account**: Whether the customer has a certificate of deposit account
- **Online**: Whether the customer uses online banking
- **CreditCard**: Whether the customer has a credit card with the bank
- **Personal Loan (Target)**: Whether the customer accepted the personal loan (1 = Yes, 0 = No)

## 🚀 Project Workflow
1. **Exploratory Data Analysis (EDA)**: 
   - Handling missing values
   - Checking distributions and outliers
   - Feature engineering (if needed)
2. **Data Preprocessing**:
   - Scaling numerical features
   - Handling class imbalance (if applicable)
3. **Model Selection & Training**:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Performance evaluation using metrics like accuracy, precision, recall, F1-score, and AUC-ROC
4. **Model Evaluation & Insights**:
   - Confusion matrix visualization (heatmap)
   - ROC Curve comparison

## 📊 Results & Insights
- The **Random Forest model** provided the best accuracy and AUC-ROC score.
- The **most influential factors** in predicting loan adoption were **income, credit card spending, and education level**.
- Class imbalance was present but did not lead to overfitting due to proper model tuning.



## 📌 Key Files
- `personal_loan_analysis.ipynb` → Jupyter Notebook with EDA and model training
- `train_model.py` → Script to train and evaluate models
- `random_forest_model.pkl` → Saved Random Forest model
- `requirements.txt` → List of required Python libraries

## 📈 Visualizations
- **Feature distributions**
- **Confusion matrices**
- **ROC Curve comparisons**



## 👨‍💻 Author
**cheedi pavan kumar**  
📧 Email: your.email@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/pavankumarcheedi)  
🔗 [GitHub](https://github.com/pavankumarcheedi)  


🔹 If you found this project useful, **star⭐ the repository** and contribute! 🚀


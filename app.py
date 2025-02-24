import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained XGBoost pipeline model
with open("xgboost_pipeline.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define correct feature order based on training data
feature_order = ['age', 'job', 'marital', 'education', 'default', 'balance', 
                 'housing', 'loan', 'contact', 'day', 'month', 'duration', 
                 'campaign', 'pdays', 'previous', 'poutcome']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input in correct order
        input_data = [request.form.get(feature) for feature in feature_order]

        # Convert numerical values to appropriate type
        numerical_features = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
        for i in range(len(input_data)):
            if feature_order[i] in numerical_features:
                input_data[i] = float(input_data[i])

        # Convert input to DataFrame
        df = pd.DataFrame([input_data], columns=feature_order)

        # Make prediction
        prediction = model.predict(df)

        # Convert prediction to readable output
        result = "Subscribed" if prediction[0] == 1 else "Not Subscribed"

        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)

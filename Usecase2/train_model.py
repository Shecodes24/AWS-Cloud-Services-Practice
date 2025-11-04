import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load processed data
df = pd.read_csv('processed_data.csv')

# Features and target
X = df[['feature1', 'feature2']]
y = df['target']

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'smv_predictor_v1.joblib')

print("Model trained and saved successfully!")

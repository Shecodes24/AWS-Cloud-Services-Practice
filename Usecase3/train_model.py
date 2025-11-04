import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset: demand, supply, and price
data = pd.DataFrame({
    'demand': [50, 60, 70, 80, 90, 100, 110, 120],
    'supply': [40, 50, 55, 60, 65, 70, 75, 80],
    'price':  [200, 220, 250, 280, 310, 330, 350, 370]
})

# Features and target variable
X = data[['demand', 'supply']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model as model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")

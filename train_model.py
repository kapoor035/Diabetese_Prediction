import pandas as pd # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
import pickle

# Load dataset
data = pd.read_csv("diabetes.csv")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("diabetes-prediction-rfc-model.pkl", "wb"))

print("Model trained successfully!")
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import pickle

# Load your dataset
data = pd.read_csv("phishing_data.csv")  # replace with your actual file
X = data.drop("label", axis=1)           # replace "label" with your target column
y = data["label"]

# Train the model
gbc = GradientBoostingClassifier()
gbc.fit(X, y)

# Save the new model
with open("model_url.pkl", "wb") as f:
    pickle.dump(gbc, f)

print("Model retrained and saved successfully!")
data = pd.read_csv("phishing_data.csv")

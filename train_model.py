# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("iris.csv")
X = df.drop("species", axis=1)
y = df["species"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "app/model.joblib")
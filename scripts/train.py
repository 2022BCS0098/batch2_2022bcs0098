import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

# LOAD DATA
df = pd.read_csv("dataset/winequality-red.csv", sep=";")

X = df.drop("quality", axis=1)
y = df["quality"]

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# MODEL
model = XGBRegressor(n_estimators=100)
model.fit(X_train, y_train)

# EVALUATE
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# SAVE
joblib.dump(model, "model.pkl")

with open("metrics.json", "w") as f:
    json.dump({"r2": float(r2), "mse": float(mse)}, f)

print("XGBOOST TRAINING RUN")
print("batch2_2022bcs0098")
print(f"R2 Score: {r2}")
print(f"MSE: {mse}")

import pandas as pd

columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

data = pd.read_csv(
    "processed.cleveland.data",
    names=columns,
    na_values="?"
)

# Convert UCI codes to the codes used by the prediction form

# Chest pain: UCI 1-4 -> Form 0-3
data["cp"] = data["cp"] - 1

# ST slope: UCI 1-3 -> Form 0-2
data["slope"] = data["slope"] - 1

# Thalassemia: UCI 3/6/7 -> Form 1/2/3
data["thal"] = data["thal"].replace({
    3: 1,
    6: 2,
    7: 3
})

# Convert target into binary classification
# 0 = no heart disease
# 1,2,3,4 = heart disease
data["target"] = data["target"].apply(lambda x: 0 if x == 0 else 1)

# Remove rows containing missing values
data = data.dropna()

# Save cleaned dataset
data.to_csv("heart.csv", index=False)

print("heart.csv created successfully!")
print(data.head())
print("\nDataset shape:", data.shape)
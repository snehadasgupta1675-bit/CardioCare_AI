import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, f1_score


# Load dataset
data = pd.read_csv("heart.csv")

# Input features
X = data.drop("target", axis=1)

# Target
y = data["target"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# Models
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC())
    ]),

    "Naive Bayes": GaussianNB(),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}


best_model = None
best_accuracy = 0
best_name = ""


# Train and evaluate models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print("\n", name)
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("F1 Score:", round(f1 * 100, 2), "%")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_name = name


# Save the best model
joblib.dump(best_model, "heart_model.pkl")

print("\n-----------------------------")
print("Best Model:", best_name)
print("Best Accuracy:", round(best_accuracy * 100, 2), "%")
print("Model saved as heart_model.pkl")
print("-----------------------------")
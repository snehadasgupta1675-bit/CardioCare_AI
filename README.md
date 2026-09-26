# CardioCare AI – AI-Based Heart Disease Risk Assessment System

## 📌 Project Overview

CardioCare AI is an Artificial Intelligence and Machine Learning-based web application developed to provide an educational and informational assessment of possible heart disease risk.

The system allows a user to enter different health-related and clinical parameters through a user-friendly web interface. The submitted information is processed by a Django backend and passed to a trained Machine Learning model. The trained Support Vector Machine (SVM) model analyses the input data and produces a heart disease risk classification.

The system displays the result in a simple form:

- Higher Risk of Heart Disease
- Lower Risk of Heart Disease

CardioCare AI is developed as an educational project to demonstrate how Machine Learning can be integrated with a real-world web application.

> ⚠️ Medical Disclaimer: CardioCare AI is intended only for educational and informational purposes. It does not provide a medical diagnosis and should not be used as a substitute for professional medical advice, diagnosis, or treatment.


## 🎯 Objectives

The main objectives of CardioCare AI are:

- To develop a Machine Learning-based heart disease risk assessment system.
- To apply Artificial Intelligence to structured health-related data.
- To compare multiple Machine Learning classification algorithms.
- To select a suitable model based on Accuracy and F1-Score.
- To integrate the trained Machine Learning model with a Django web application.
- To provide a simple and user-friendly prediction interface.
- To demonstrate the practical use of Machine Learning in a health-related application.
- To provide an educational platform for understanding AI-based risk assessment.


## ✨ Main Features

### 🏠 Home Page

The Home Page introduces CardioCare AI and explains the purpose of the system. It provides information about heart health, the general working process, important health indicators, and healthy habits.

### ⭐ Features Page

The Features page explains the major capabilities of the system, including:

- User-friendly interface
- Machine Learning-based prediction
- Structured health-data processing
- Quick prediction processing
- Simple result presentation

### 📚 Information Page

The Information page provides educational information related to heart health and the factors considered by the system.

### 🧮 Prediction Tool

The Prediction Tool allows users to enter the health-related parameters required by the Machine Learning model.

The form includes:

1. Name
2. Age
3. Gender
4. Chest Pain Type
5. Resting Blood Pressure
6. Cholesterol Level
7. Fasting Blood Sugar
8. Resting ECG Results
9. Maximum Heart Rate
10. Exercise-Induced Angina
11. ST Depression
12. ST Slope
13. Number of Major Vessels
14. Thalassemia Status

### 📊 Prediction Result

After submitting the form, the trained Machine Learning model processes the input and the system displays either:

**Higher Risk of Heart Disease**

or

**Lower Risk of Heart Disease**

The result is presented in a simple and understandable format.


## 🤖 Machine Learning

CardioCare AI uses supervised Machine Learning classification techniques to classify health-related records into two target categories:

- `0` – No Heart Disease
- `1` – Heart Disease

Four Machine Learning algorithms were implemented and compared:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Naïve Bayes
4. Random Forest

The models were evaluated using:

- Accuracy
- F1-Score


## 🏆 Model Evaluation

The dataset was divided into training and testing portions using a 75:25 stratified train-test split.

The obtained results were:

| Model | Accuracy | F1-Score |
|---|---:|---:|
| Logistic Regression | 85.33% | 84.06% |
| Support Vector Machine (SVM) | 86.67% | 85.29% |
| Naïve Bayes | 85.33% | 84.51% |
| Random Forest | 85.33% | 84.06% |

Based on the project evaluation, Support Vector Machine (SVM) achieved the highest Accuracy and F1-Score among the evaluated models.

Therefore, SVM was selected as the final Machine Learning model used by the CardioCare AI web application.


## 📁 Dataset

The project uses the UCI Heart Disease Cleveland dataset.

After preprocessing and removal of incomplete records, the working dataset contains:

- 297 records
- 13 input features
- 1 binary target column

### Input Features

| Feature | Description |
|---|---|
| `age` | Age |
| `sex` | Sex |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Cholesterol level |
| `fbs` | Fasting blood sugar |
| `restecg` | Resting ECG result |
| `thalach` | Maximum heart rate |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression |
| `slope` | Exercise ST-segment slope |
| `ca` | Number of major vessels |
| `thal` | Thalassemia status |

### Target

The target column is converted into binary classification:

- `0` = No Heart Disease
- `1` = Heart Disease


## 🔄 System Workflow

The overall working process of CardioCare AI is:

```text
User
  ↓
CardioCare AI Web Interface
  ↓
Prediction Form
  ↓
Django Backend
  ↓
Input Processing
  ↓
13 Health-Related Features
  ↓
Trained SVM Model
  ↓
Prediction
  ↓
Higher Risk / Lower Risk
  ↓
Result Page


The user enters the required health information through the Prediction Tool. Django receives the submitted values and converts them into the required numerical format.
The 13 features are arranged in the same order used during model training. The processed values are then passed to the trained SVM model stored as heart_model.pkl.
The model generates a binary prediction, which is converted into an understandable result and displayed on the result page.

🧹 Data Preprocessing

The dataset is prepared before Machine Learning model training.

The preprocessing process includes:

Reading the original dataset.
Identifying missing values.
Removing incomplete records.
Converting categorical values into the required numerical representation.
Converting the original target values into binary classes.
Creating the cleaned heart.csv dataset.
Separating input features and the target variable.
Splitting the data into training and testing sets.

The final cleaned dataset contains 297 records.

📏 Feature Scaling

Feature scaling is applied to the models that require standardized numerical input.

CardioCare AI uses:

StandardScaler()

StandardScaler is used with Logistic Regression and Support Vector Machine through a Machine Learning Pipeline.

This helps place numerical features with different ranges onto a comparable scale before classification.

🧠 Final Machine Learning Model

The final model selected for the application is:

Support Vector Machine (SVM)

The model is implemented using a Pipeline:

"SVM": Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC())
])

The trained model is saved as:

heart_model.pkl

The Django application loads this trained model and uses it to process new prediction inputs.

🌐 Technologies Used
Programming Language
Python
Web Framework
Django
Frontend
HTML
CSS
JavaScript
Machine Learning
Scikit-learn
Data Processing
Pandas
NumPy
Model Saving and Loading
Joblib
Development Environment
Visual Studio Code
Version Control
Git
GitHub

Deployment
Render
📂 Project Structure
CardioCare_AI/
│
├── cardiocare/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── prediction/
│   ├── views.py
│   └── heart_model.pkl
│
├── dataset/
│   ├── processed.cleveland.data
│   ├── create_dataset.py
│   ├── train_model.py
│   └── heart.csv
│
├── templates/
│   ├── home.html
│   ├── features.html
│   ├── information.html
│   ├── prediction.html
│   ├── resources.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── heart.png
│
├── build.sh
├── manage.py
├── requirements.txt
├── .gitignore
└── db.sqlite3

Note: The exact folder arrangement may vary slightly depending on the local Django project structure.

⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/CardioCare_AI.git

Move into the project directory:

cd CardioCare_AI
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment

For Windows:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Run Database Migrations
python manage.py migrate
6. Collect Static Files
python manage.py collectstatic --no-input
7. Run the Development Server
python manage.py runserver

The application can then be opened in a browser using the local Django server address.

🚀 Deployment

CardioCare AI is prepared for deployment using Render.

The project includes:

requirements.txt
build.sh

The build.sh file contains the commands required to install Python dependencies and collect Django static files.

The production application can be started using Gunicorn.

🔐 Project Safety

The project follows basic development practices such as:

Using .gitignore for unnecessary files.
Keeping the virtual environment outside version control.
Separating frontend and backend components.
Using a trained model file for prediction.
Processing user input through Django.
Providing a clear medical disclaimer.
⚠️ Limitations

CardioCare AI has several limitations:

Dataset Limitation

The model is trained using a specific heart disease dataset containing 297 cleaned records. Therefore, the model may not represent every population or every possible health condition.

Input Limitation

The prediction depends on the accuracy of the information entered by the user. Incorrect or incomplete information may affect the prediction.

Model Limitation

The final SVM model achieved 86.67% Accuracy and 85.29% F1-Score on the project's test dataset. These results do not guarantee the same performance for every new user or real-world medical situation.

🏥 Medical Safety

CardioCare AI is not a medical diagnosis system.

The prediction generated by the application is a Machine Learning-based computational risk assessment and should not be used to:

Diagnose a medical condition.
Replace a doctor's evaluation.
Make emergency medical decisions.
Decide whether medication or treatment is required.

Users with health concerns should consult a qualified healthcare professional.

🔮 Future Enhancements

Possible future improvements include:

Using larger and more diverse datasets.
Testing additional Machine Learning algorithms.
Hyperparameter tuning.
More advanced model validation.
Additional performance metrics.
Improved input validation.
User authentication.
Better data security.
Responsive design improvements.
Secure cloud deployment.
More detailed educational feedback.
Integration with additional health-related data sources.
📌 Learning Outcomes

This project provided practical experience in:

Python programming
Django web development
Machine Learning
Data preprocessing
Feature scaling
Classification algorithms
Model evaluation
Pandas and NumPy
Scikit-learn
Joblib
HTML, CSS, and JavaScript
Git and GitHub
Web application deployment
👩‍💻 Developer

Sneha Dasgupta

BCA Student
George College

Project: CardioCare AI – AI-Based Heart Disease Risk Assessment System

📜 Project Purpose

CardioCare AI was developed as an academic and educational project to demonstrate the practical implementation of Artificial Intelligence and Machine Learning in a web-based health risk assessment application.

The project combines data science, Machine Learning, Django web development, and user interface design into one complete application.

⭐ Acknowledgement

This project was developed as part of academic learning and practical project work. The development process provided an opportunity to understand how a Machine Learning model can be trained, evaluated, saved, and integrated into a Django web application.

📄 License

This project is developed for educational and academic purposes.

The project and its Machine Learning prediction should not be considered a certified medical software product.

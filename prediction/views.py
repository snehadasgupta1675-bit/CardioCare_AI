from django.shortcuts import render
import joblib
import os
import numpy as np
from django.conf import settings


# Load the trained model
MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "prediction",
    "heart_model.pkl"
)

model = joblib.load(MODEL_PATH)


def home(request):
    return render(request, "home.html")


def features(request):
    return render(request, "features.html")


def information(request):
    return render(request, "information.html")


def resources(request):
    return render(request, "resources.html")


def prediction(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = float(request.POST.get("age"))
        sex = float(request.POST.get("sex"))
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = float(request.POST.get("fbs"))
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = float(request.POST.get("exang"))
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))

        # Arrange values in the same order as the training dataset
        features_data = np.array([[
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        # Make prediction
        result = model.predict(features_data)[0]

        if result == 1:
            prediction_result = "Higher Risk of Heart Disease"
        else:
            prediction_result = "Lower Risk of Heart Disease"

        return render(
            request,
            "result.html",
            {
                "name": name,
                "result": prediction_result
            }
        )

    return render(request, "prediction.html")
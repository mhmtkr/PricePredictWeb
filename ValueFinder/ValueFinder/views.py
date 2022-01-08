from django.shortcuts import render

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request, "home.html")
def predict(request):
    return render(request, "predict.html")
def result(request):

    # Load dataset
    data = pd.read_csv(r"C:/Users/Acer/Desktop/Data/Housing.csv")
    data = data.drop(['Address'], axis=1)

    # Train test split
    X = data.drop(['Price'], axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=.30)

    # Train
    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Predict
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])

    pred = model.predict(np.array([val1, val2, val3, val4, val5]).reshape(1, -1))
    pred = round(pred[0])

    price = "The predicted price is $" + str(pred)

    # Assign the value ot the "price" to the "result2" variable in "predict.html"
    return render(request, "predict.html", {"result2":price})


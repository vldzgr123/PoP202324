import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import *


class RegressionModel:
    data = None
    y_pred = None
    model = None
    y_test = None

    def __init__(self, data):
        self.data = data

    def ClearData(self):
        self.data.drop(
            ["id", "zipcode", "lat", "long", "date", "sqft_lot15", "sqft_living15"],
            inplace=True,
            axis=1,
        )
        self.data["floors"] = self.data["floors"].astype(int)
        self.data["sqft_living"] = self.data["sqft_living"].astype(float)
        self.data = self.data[self.data.price <= 7000000]
        self.data = self.data[self.data.bedrooms <= 8]
        self.data = self.data[self.data.bathrooms <= 5]
        self.data = self.data[self.data.sqft_living <= 6000]
        self.data = self.data[self.data.sqft_above <= 5500]
        self.data = self.data[self.data.sqft_basement <= 2000]

    def FitPredict(self):
        y = self.data["price"]
        X = self.data.drop(["price"], axis=1)
        X_train, X_test, y_train, self.y_test = train_test_split(X, y, test_size=0.2)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        params_grid = {
            "alpha": [1e-9, 1e-10, 1e-11],
            "kernel": [
                DotProduct(),
                WhiteKernel(),
                RBF(),
            ]
        }
        self.model = GridSearchCV(GaussianProcessRegressor(), params_grid).fit(
            X_train, y_train
        )
        self.y_pred = self.model.predict(X_test)

    def GetPrediction(self):
        return self.y_pred

    def GetTest(self):
        return self.y_test

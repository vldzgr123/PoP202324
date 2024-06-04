import streamlit as st
import pandas as pd
from CART import *
import time
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import NearMiss
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score,
    accuracy_score,
)
from sklearn.preprocessing import StandardScaler
from math import sqrt

def Metrics(y_test, y_pred, typeModel):
    if typeModel == "Классификация":
        st.write(f'accuracy: {accuracy_score(y_test, y_pred)}')
    else:
        st.write(f'MAE: {mean_absolute_error(y_test, y_pred)}')
        st.write(f'MSE: {mean_squared_error(y_test, y_pred)}')
        st.write(f'RMSE: {sqrt(mean_squared_error(y_test, y_pred))}')
        st.write(f'MAPE: {sqrt(mean_absolute_percentage_error(y_test, y_pred))}')
        st.write(f'R^2: {r2_score(y_test, y_pred)}')

st.title("Практикум по программированию. Лабораторная работа №3.")
st.header("CART")

typeModel = st.selectbox("Выберите тип задачи:", ["Регрессия", "Классификация"])
uploaded_file = st.file_uploader("Выберите файл датасет", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    max_depth = st.number_input("Максимальная глубина:", min_value=2, max_value=15)
    min_samples_split = st.number_input("Минимальное количество образцов для разбиения:", min_value=2, max_value=15)
    button_clean = st.button("Начать очистку данных и обучение модели")
    if button_clean:
        st.write("Очистка и обучение....")
        time.sleep(5)
        if typeModel == "Классификация":
            data_class = data
            data_class.drop(["A_id"], axis=1, inplace=True)
            data_class.dropna(inplace=True)
            data_class["Acidity"] = data_class["Acidity"].astype(float)
            data_class["Quality"] = data_class["Quality"].map({"good": 1, "bad": 0})
            X = data_class.drop("Quality", axis=1)
            y = data_class["Quality"].values
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            scaler = StandardScaler()
            scaler.fit(X_train)
            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test)
            nm = NearMiss()
            X_train, y_train = nm.fit_resample(X_train, y_train.ravel())
            model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
        else:
            data_reg = data
            categorical_col = [
                "mainroad",
                "guestroom",
                "basement",
                "hotwaterheating",
                "airconditioning",
                "prefarea",
            ]
            data_reg[categorical_col] = data_reg[categorical_col].apply(
                lambda x: x.map({"yes": 1, "no": 0})
            )
            dummy_col = pd.get_dummies(data_reg['furnishingstatus']).astype(int)
            data_reg = pd.concat([data_reg, dummy_col], axis = 1)
            data_reg.drop(['furnishingstatus'], axis = 1, inplace = True)
            X = data_reg.drop("price", axis=1)
            y = data_reg['price'].values
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            scaler=StandardScaler()
            scaler.fit(X_train)
            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test)
            model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
        st.write("Обучение завершено.")
        Metrics(y_test, y_pred, typeModel)
        
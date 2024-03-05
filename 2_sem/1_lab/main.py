import streamlit as st
import pandas as pd
from function.predict import *
from function.visualization import *
from function.description import *
from function.featuresSelect import *


st.title("Практикум по программированию. Лабораторная работа №1.")
st.header("Обучение модели машинного обучения с помощью алгоритма Gaussian Processes")

typeModel = st.selectbox("Выберите тип задачи:", ["Регрессия", "Классификация"])
uploaded_file = st.file_uploader("Выберите файл датасет", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    Description(typeModel=typeModel).Show()
    Visualization(data=data, typeModel=typeModel).Show()

    data = FeaturesSelect(typeModel=typeModel).Select()
    button = st.button("Предсказать")
    if button:
        Predict(data=data, typeModel=typeModel).Predict()

import streamlit as st
import pandas as pd
from function.description import descriptionClassification, descriptionRegression
from function.regressionModel import *
from function.visualization import *
from function.functionMetrics import *


st.title("Практикум по программированию. Лабораторная работа №1.")
st.header("Обучение модели машинного обучения с помощью алгоритма Gaussian Processes")

typeTask = st.selectbox("Выберите тип задачи:", ["Регрессия", "Классификация"])
uploaded_file = st.file_uploader("Выберите файл датасет", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if typeTask == "Регрессия":
        st.header("Описание и визуализация датасета")
        descriptionRegression()
        
        visualizationRegression = VisualizationDataRegression(data)
        visualizationRegression.BarChart()
        visualizationRegression.BoxPlot()
        visualizationRegression.HeatMap()
        visualizationRegression.PieСhart()
        
        regressionModel = RegressionModel(data)
        regressionModel.ClearData()
        regressionModel.FitPredict()
        
        metrics = Metrics(RegressionModel.GetTest(), RegressionModel.GetPrediction())

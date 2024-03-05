import pandas as pd
import pickle
import streamlit as st
from sklearn.gaussian_process.kernels import *


class Predict:
    def __init__(self, data, typeModel):
        self.data = data
        self.typeModel = typeModel

    def Predict(self):
        st.write("Предсказанное значение")
        if self.typeModel == "Регрессия":
            with open("models/regressionModel.pickle", "rb") as file:
                reg = pickle.load(file)
            reg_pred = reg.predict(self.data)[0]
            st.write(round(reg_pred))
        else:
            with open("models/classificationModel.pickle", "rb") as file:
                cl = pickle.load(file)
            cl_pred = cl.predict(self.data)[0]
            st.write(round(cl_pred))

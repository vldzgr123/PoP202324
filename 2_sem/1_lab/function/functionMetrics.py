from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score,
    classification_report,
)
from math import sqrt
import streamlit as st


class Metrics:
    def __init__(self, y_test, y_pred):
        self.y_test = y_test
        self.y_pred = y_pred

    def Regression(self):
        st.write(f"MAE: {mean_absolute_error(self.y_test, self.y_pred)}")
        st.write(f"MSE: {mean_squared_error(self.y_test, self.y_pred)}")
        st.write(f"RMSE: {sqrt(mean_squared_error(self.y_test, self.y_pred))}")
        st.write(
            f"MAPE: {sqrt(mean_absolute_percentage_error(self.y_test, self.y_pred))}"
        )
        st.write(f"R^2: {r2_score(self.y_test, self.y_pred)}")

    def Classification(self):
        st.write(classification_report(self.y_test, self.y_pred))

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


class VisualizationDataClassification:
    def __init__(self, data):
        self.data = data

    def HeatMap(self):
        st.write("Тепловая карта")
        df_num = self.data.select_dtypes(include=np.number)
        df_corr = df_num.corr()
        plt.figure(figsize=(16, 6))
        sns.heatmap(df_corr, annot=True)
        st.pyplot(plt)

    def BoxPlot(self):
        st.write("Ящик с усами")
        df_num = self.data.select_dtypes(include=np.number)
        plt.figure(figsize=(16, 8))
        for i, column in enumerate(df_num.columns):
            plt.subplot(3, 8, i + 1)
            sns.boxplot(data=df_num, y=column)
            plt.title(column)

        plt.tight_layout()
        st.pyplot(plt)

    def BarChart(self):
        st.write("Гистограмма")
        columns = ["ct_money", "t_money"]
        for col in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.data[col], bins=100, kde=True)
            plt.title(f"Гистограмма для {col}")
            st.pyplot(plt)
            
    def PieСhart(self):
        st.write("Круговая диаграмма")
        plt.figure(figsize=(8, 8))
        self.data["bomb_planted"].value_counts().plot.pie(autopct="%1.1f%%")
        plt.title("bomb_planted")
        plt.ylabel("")
        st.pyplot(plt)
        
class VisualizationDataRegression:
    def __init__(self, data):
        self.data = data

    def HeatMap(self):
        st.write("Тепловая карта")
        df_num = self.data.select_dtypes(include=np.number)
        df_corr = df_num.corr()
        plt.figure(figsize=(16, 6))
        sns.heatmap(df_corr, annot=True)
        st.pyplot(plt)

    def BoxPlot(self):
        st.write("Ящик с усами")
        df_num = self.data.select_dtypes(include=np.number)
        plt.figure(figsize=(16, 8))
        for i, column in enumerate(df_num.columns):
            plt.subplot(3, 8, i + 1)
            sns.boxplot(data=df_num, y=column)
            plt.title(column)

        plt.tight_layout()
        st.pyplot(plt)

    def BarChart(self):
        st.write("Гистограмма")
        columns = ["price", "sqft_living"]
        for col in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.data[col], bins=100, kde=True)
            plt.title(f"Гистограмма для {col}")
            st.pyplot(plt)
            
    def PieСhart(self):
        st.write("Круговая диаграмма")
        plt.figure(figsize=(8, 8))
        self.data["floors"].value_counts().plot.pie(autopct="%1.1f%%")
        plt.title("floors")
        plt.ylabel("")
        st.pyplot(plt)

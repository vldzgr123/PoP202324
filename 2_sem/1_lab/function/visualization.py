import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


class Visualization:
    def __init__(self, data, typeModel):
        self.data = data
        self.typeModel = typeModel

    def VisualizationClassification(self):

        st.write("Тепловая карта")
        df_num = self.data.select_dtypes(include=np.number)
        df_corr = df_num.corr()
        plt.figure(figsize=(16, 6))
        sns.heatmap(df_corr, annot=True)
        st.pyplot(plt)

        st.write("Ящик с усами")
        df_num = self.data.select_dtypes(include=np.number)
        plt.figure(figsize=(16, 8))
        for i, column in enumerate(df_num.columns):
            plt.subplot(3, 8, i + 1)
            sns.boxplot(data=df_num, y=column)
            plt.title(column)

        plt.tight_layout()
        st.pyplot(plt)

        st.write("Гистограмма")
        columns = ["Size", "Weight"]
        for col in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.data[col], bins=100, kde=True)
            plt.title(f"Гистограмма для {col}")
            st.pyplot(plt)

        st.write("Круговая диаграмма")
        plt.figure(figsize=(8, 8))
        self.data["Quality"].value_counts().plot.pie(autopct="%1.1f%%")
        plt.title("Quality")
        plt.ylabel("")
        st.pyplot(plt)

    def VisualizationRegression(self):

        st.write("Тепловая карта")
        df_num = self.data.select_dtypes(include=np.number)
        df_corr = df_num.corr()
        plt.figure(figsize=(16, 6))
        sns.heatmap(df_corr, annot=True)
        st.pyplot(plt)

        st.write("Ящик с усами")
        df_num = self.data.select_dtypes(include=np.number)
        plt.figure(figsize=(16, 8))
        for i, column in enumerate(df_num.columns):
            plt.subplot(3, 8, i + 1)
            sns.boxplot(data=df_num, y=column)
            plt.title(column)

        plt.tight_layout()
        st.pyplot(plt)

        st.write("Гистограмма")
        columns = ["price", "area"]
        for col in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.data[col], bins=100, kde=True)
            plt.title(f"Гистограмма для {col}")
            st.pyplot(plt)

        st.write("Круговая диаграмма")
        plt.figure(figsize=(8, 8))
        self.data["stories"].value_counts().plot.pie(autopct="%1.1f%%")
        plt.title("stories")
        plt.ylabel("")
        st.pyplot(plt)

    def Show(self):
        st.header("Вузуализация датасета")
        if self.typeModel == "Регрессия":
            self.VisualizationRegression()
        else:
            self.VisualizationClassification()

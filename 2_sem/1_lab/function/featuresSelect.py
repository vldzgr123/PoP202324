import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class FeaturesSelect:
    def __init__(self, typeModel):
        self.typeModel = typeModel

    def Select(self):
        st.header("Ручной ввод признаков")
        if self.typeModel == "Классификация":
            Size = st.number_input(
                "Size: Размер плода:",
                value=-7.151703,
                min_value=-7.151703,
                max_value=6.406367,
            )

            Weight = st.number_input(
                "Weight: Вес плода:",
                value=-7.149848,
                min_value=-7.149848,
                max_value=5.790714,
            )

            Sweetness = st.number_input(
                "Sweetness: Степень сладости фруктов",
                value=-6.894485,
                min_value=-6.894485,
                max_value=6.374916,
            )

            Crunchiness = st.number_input(
                "Crunchiness: текстура, указывающая на хрусткость фруктов",
                value=-6.055058,
                min_value=-6.055058,
                max_value=7.619852,
            )
            Juiciness = st.number_input(
                "Juiciness: Уровень сочности плодов",
                value=-5.961897,
                min_value=-5.961897,
                max_value=7.364403,
            )

            Ripeness = st.number_input(
                "Ripeness: Стадия спелости плодов",
                value=-5.864599,
                min_value=-5.864599,
                max_value=7.237837,
            )

            Acidity = st.number_input(
                "Acidity: уровень кислотности фруктов",
                value=1.510493,
                min_value=1.510493,
                max_value=7.404736,
            )

            data = pd.DataFrame(
                {
                    "Size": [Size],
                    "Weight": [Weight],
                    "Sweetness": [Sweetness],
                    "Crunchiness": [Crunchiness],
                    "Juiciness": [Juiciness],
                    "Ripeness": [Ripeness],
                    "Acidity": [Acidity],
                }
            )

            return data

        else:
            
            area = st.number_input(
                "area - площадь:",
                value=1650,
                min_value=1650,
                max_value=16200
            )

            bedrooms = st.number_input(
                "bedrooms - кол-во спальных комнат",
                value=1,
                min_value=1,
                max_value=6
            )

            bathrooms = st.number_input(
                "bathrooms - кол-во ванных комнат:",
                value=1,
                min_value=1,
                max_value=4
            )
            
            stories = st.number_input(
                "stories - история",
                value=1,
                min_value=1,
                max_value=4
            )

            mainroad = st.selectbox("mainroad - на главной ли дороге", ["yes", "no"])
            guestroom = st.selectbox("guestroom - есть ли гостевая комната", ["yes", "no"])
            basement = st.selectbox("basement - подвал", ["yes", "no"])
            hotwaterheating = st.selectbox("hotwaterheating - водяное отопление", ["yes", "no"])
            airconditioning = st.selectbox("airconditioning - есть ли система кондиционирования воздуха", ["yes", "no"])
            parking = st.number_input(
                "parking - сколько парковок",
                value=0,
                min_value=0,
                max_value=3
            )
            prefarea = st.selectbox("prefarea - есть ли предварительная аренда", ["yes", "no"])
            statuses = ["furnished", "semi-furnished", "unfurnished"]
            furnishingstatus = st.selectbox("furnishingstatus - состоние мебелирование", statuses)
            
            furnished = 0
            semifurnished = 0
            unfurnished = 0
            
            if furnishingstatus == "furnished":
                furnished = 1
            elif furnishingstatus == "semi-furnished": 
                semifurnished = 1
            else:
                unfurnished = 1

            data = pd.DataFrame(
                {
                    "area": [area],
                    "bedrooms": [bedrooms],
                    "bathrooms": [bathrooms],
                    "stories": [stories],
                    "mainroad": [mainroad],
                    "guestroom": [guestroom],
                    "basement": [basement],
                    "hotwaterheating": [hotwaterheating],
                    "airconditioning": [airconditioning],
                    "parking": [parking],
                    "prefarea": [prefarea],
                    "furnished" : [furnished],
                    "semi-furnished" : [semifurnished],
                    "unfurnished" : [unfurnished]
                }
            )
            
            categorical_col = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
            data[categorical_col] = data[categorical_col].apply(
                lambda x: x.map({"yes": 1, "no": 0})
            )
            
            return data

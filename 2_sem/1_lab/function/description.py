import streamlit as st


class Description:

    def __init__(self, typeModel):
        self.typeModel = typeModel

    def DescriptionClassification(self):
        st.write("A_id: Уникальный идентификатор для каждого фрукта")
        st.write("Size: Размер плода")
        st.write("Weight: Вес плода")
        st.write("Sweetness: Степень сладости фруктов")
        st.write("Crunchiness: текстура, указывающая на хрусткость фруктов")
        st.write("Juiciness: Уровень сочности плодов")
        st.write("Ripeness: Стадия спелости плодов")
        st.write("Acidity: уровень кислотности фруктов")
        st.write("Quality: Общее качество плодов")

    def DescriptionRegression(self):
        st.write("price - цена")
        st.write("area - площадь")
        st.write("bedrooms - кол-во спальных комнат")
        st.write("bathrooms - кол-во ванных комнат")
        st.write("stories - история")
        st.write("mainroad - на главной ли дороге")
        st.write("guestroom - есть ли гостевая комната")
        st.write("basement - подвал")
        st.write("hotwaterheating - водяное отопление")
        st.write("airconditioning - есть ли система кондиционирования воздуха")
        st.write("parking - сколько парковок")
        st.write("prefarea - есть ли предварительная аренда")
        st.write("furnishingstatus - состоние мебелирование")

    def Show(self):
        st.header("Описание признаков датасета")
        if self.typeModel == "Регрессия":
            self.DescriptionRegression()
        else:
            self.DescriptionClassification

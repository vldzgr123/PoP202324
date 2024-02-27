import streamlit as st


def descriptionRegression():
    st.write("price - цена")
    st.write("bedrooms - кол-во спальных комнат")
    st.write("bathrooms - кол-во ванных комнат")
    st.write("sqft_living - площадь жилых помещений")
    st.write("floors - этажи")
    st.write("waterfront - набережная (0 или 1)")
    st.write("view - вид (0 или 1)")
    st.write("grade - класс (от 1 до 13)")
    st.write("sqft_above - площадь дома исключая подвал")
    st.write("sqft_basement - площадь подвала")
    st.write("yr_built - год строительства")
    st.write("yr_renovated - год последнего кап ремонта (если был)")
    st.write("condition - состояние дома")
    st.write("sqft_lot - площадь участка")


def descriptionClassification():
    st.write("1. time_left - длительность раунда")
    st.write("2. ct_score - количество очков у команды контр-террористов")
    st.write("3. t_score - количество очков у террористов")
    st.write("4. map - карта")
    st.write("5. bomb_planted - установлена ли бомба")
    st.write(
        "6. ct_health и t_health - суммарное здоровье контр-террористов и террористов соответственно"
    )
    st.write(
        "7. ct_armor и t_armor - суммарная броня контр-террористов и террористов соответственно"
    )
    st.write(
        "8. ct_money и t_money - суммарное количество денег контр-террористов и террористов соответственно"
    )
    st.write(
        "9. ct_helmets и t_helmets - суммарное количество шлемов контр-террористов и террористов соответственно"
    )
    st.write(
        "10. ct_defuse_kits - количество наборов обезвреживания бомбы у контр-террористов"
    )
    st.write(
        "11. ct_players_alive и t_players_alive - количество живых контр-террористов и террористов соответственно"
    )

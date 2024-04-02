from RedBlackTree import RedBlackTree
import streamlit as st

st.title('Лабораторная по дисциплине "Практикум по программированию" №2.')
st.header("Реализация Красно-черного дерева.")
numbers = st.text_input("Впишите через пробел значения дерева:").split(" ")
button = st.button("Визуализировать")
if button:
    tree = RedBlackTree(int(numbers[0]))
    for key in numbers[1::]:
        tree.Insert(int(key))

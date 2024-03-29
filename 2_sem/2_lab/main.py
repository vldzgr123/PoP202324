from RedBlackTree import RedBlackTree
import streamlit as st
import graphviz

st.title('Лабораторная по дисциплине "Практикум по программированию" №2.')
st.header("Реализация Красно-черного дерева.")
numbers = st.text_input("Впишите через пробел значения дерева:").split(" ")
if len(numbers)!=0:
    tree = RedBlackTree(numbers)
    for i in numbers[0::]:
        

# # Пример словаря для представления дерева
# tree = {
#     'Node 1': {
#         'Node 2': {
#             'Node 4': None,
#             'Node 5': None
#         },
#         'Node 3': None
#     }
# }

# def visualize_tree(tree, parent=None):
#     if tree is None:
#         return

#     for key, value in tree.items():
#         if parent:
#             graphviz.edge(parent, key)
#         visualize_tree(value, parent=key)

# st.graphviz_chart('''
#     digraph {
#         Node1 -> Node2
#         Node2 -> Node4
#         Node2 -> Node5
#         Node1 -> Node3
#     }
# ''')
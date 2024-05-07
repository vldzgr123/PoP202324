from redblacktree import RedBlackTree
import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx
import time

st.set_page_config(
    page_title="RedBlackTree",
)

session = st.session_state

if 'tree' not in session:
    session.tree = RedBlackTree()

if 'inserted_values' not in session:
    session.inserted_values = []

if 'session_iteration' not in session:
    session.session_iteration = 0

st.title('Red-Black Tree')

sidebar = st.sidebar
sidebar.title('Options')

# вставка чисел
sidebar.subheader('Insert')
sidebar.text_input(label='Insert', key='insert_field', label_visibility='collapsed')
def clear_insert_text():
    session.new_values = session.insert_field
    session["insert_field"] = ""
sidebar.button(label='Insert', key='insert_button', on_click=clear_insert_text, use_container_width=True)

sidebar.subheader('Search')
value = sidebar.text_input(label='Search', key='search_field', label_visibility='collapsed')
if sidebar.button(label='Search', key='search_button', use_container_width=True) and value:
    node = session.tree.search(int(value))
    if node:
        st.success(f'Found {value}')
    else:
        st.warning(f'No found{value}', icon='⚠️')

sidebar.subheader('Erase')
sidebar.text_input(
    label='Erase',
    key='values2delete',
    label_visibility='collapsed'
)
def clear_delete_text():
    session.deleting_values = session.values2delete
    session["values2delete"] = ""
sidebar.button(label='Erase', key='delete_button', on_click=clear_delete_text, use_container_width=True)


if session.insert_button:
    try:
        new_values = [int(value) for value in 
                      session.new_values.split()]
    except ValueError as e:
        new_values = None
        st.error(f'Incorrect enter {e}')

    correct_values = []
    wrong_values = []
    for value in new_values:
        try:
            session.tree.insert(value)
            session.inserted_values.append(value)
            correct_values.append(value)
        except ValueError:
            wrong_values.append(value)
    if correct_values:
        st.success(f'Succesfully insert {correct_values}', icon='✅')
    if wrong_values:
        st.warning(f'Failure {wrong_values}', icon='⚠️')

if session.delete_button:
    try:
        values2delete = [int(value) for value in 
            session.deleting_values.split()]
    except ValueError as e:
        values2delete = None
        st.error(f'Incorrect enter {e}')

    correct_values = []
    wrong_values = []
    for value in values2delete:
        try:
            session.tree.delete(value)
            session.inserted_values.remove(value)
            correct_values.append(value)
        except ValueError:
            wrong_values.append(value)
    if correct_values:
        st.success(f'Succesfully erase {correct_values}', icon='✅')
    if wrong_values:
        st.warning(f'Failure {wrong_values}', icon='⚠️')

if session.inserted_values:
    st.subheader(f'Nodes: {sorted(session.inserted_values)}')
    tree = session.tree
    g, pos, options = tree.realize()
    fig = plt.figure(figsize=[7]*2)
    plt.axis('off')
    nx.draw_networkx(g, pos, **options)
    st.pyplot(fig)

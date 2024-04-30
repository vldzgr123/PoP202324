from RedBlackTree import RedBlackTree
import os
import click

clear = lambda: os.system("cls")
clear()
n = int(input("Enter first element tree: "))
tree = RedBlackTree(n)
while n != "0":
    clear()
    print("------------------------------------------------------------------")
    print("1. Show tree.")
    print("2. Insert element.")
    print("0. Exit")
    print("------------------------------------------------------------------")
    n = input()
    clear()
    match n:
        case "1":
            print(tree)
            click.pause()
        case "2":
            key = int(input("Enter element: "))
            check = tree.Insert(key)
            if check: 
                print("Item added successfully!")
            else:
                print("Such an element already exists in the tree")
            click.pause()

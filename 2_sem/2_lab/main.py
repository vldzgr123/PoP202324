from RedBlackTree import RedBlackTree
import os

clear = lambda: os.system('cls')


print("Введите первый элемент красно-черного дерева:")
n = input()
tree = RedBlackTree(n)
while(n!="0"):
    clear()
    print("------------------------------------------------------------------")
    print("1. Добавить элемент")
    print("0. Выход")
    print("------------------------------------------------------------------")
    n = input()
    clear()
    match n:
        case "1":
            print("Введите элемент:")
            el = int(input())
            tree.Insert(el)
            
            
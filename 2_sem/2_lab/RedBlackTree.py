from platform import node
from typing import Any


class Node:
    def __init__(self, key, isRed=True) -> None:
        self.key = key
        self.right = None
        self.left = None
        self.isRed = isRed
        self.parent = None

    def __str__(self):
        if self.parent != None and self.key != None:
            return f'({self.key} - {"RED" if self.isRed==True else "BLACK"} - PARENT {self.parent.key} - {"LEFT" if self.parent.left == self else "RIGHT"})'
        elif self.parent == None and self.key != None:
            return f'({self.key} - {"RED" if self.isRed==True else "BLACK"} - ROOT)'
        return f"(BLACK NIL)"


class RedBlackTree:
    def __init__(self, key) -> None:
        self.nil = Node(None, isRed=False)
        self.root = Node(key, isRed=False)
        self.root.right = self.nil
        self.root.left = self.nil

    def Insert(self, key) -> Any:
        if self.__search(self.root, key) != None:
            return False
        newNode = Node(key)
        current = self.root
        parent = current
        while current != self.nil:
            parent = current
            if current.key <= key:
                current = current.right
            else:
                current = current.left
        newNode.parent = parent
        if parent.key <= key:
            parent.right = newNode
        else:
            parent.left = newNode
        newNode.right = self.nil
        newNode.left = self.nil
        self.__fixInsert(newNode)
        return True

    def __fixInsert(self, n) -> None:
        u = self.__getUncle(n)
        g = self.__getGrandparent(n)
        if n.parent.isRed == True:
            if u.isRed == True:
                self.__fixUncleRed(n)
            else:
                if g.left == n.parent:
                    if n.parent.left == n:
                        self.__smallRotateRight(n.parent)
                        n.parent.isRed = False
                        n.parent.right.isRed = True
                    else:
                        self.__smallRotateLeft(n)
                        self.__smallRotateRight(n)
                        n.isRed = False
                        n.right.isRed = True
                else:
                    if n.parent.right == n:
                        self.__smallRotateLeft(n.parent)
                        n.parent.isRed = False
                        n.parent.left.isRed = True
                    else:
                        self.__smallRotateRight(n)
                        self.__smallRotateLeft(n)
                        n.isRed = False
                        n.left.isRed = True
                        

    def __smallRotateRight(self, n):
        p = n.parent
        g = self.__getGrandparent(n)
        n.parent = g
        p.parent = n
        if p != self.root:
            if g.left == p:
                g.left = n
            else:
                g.right = n
        else:
            self.root = n
        p.left = n.right
        n.right = p

    def __smallRotateLeft(self, n):
        p = n.parent
        g = self.__getGrandparent(n)
        n.parent = g
        p.parent = n
        if p != self.root:
            if g.left == p:
                g.left = n
            else:
                g.right = n
        else:
            self.root = n
        p.right = n.left
        n.left = p

    def __fixUncleRed(self, n):
        u = self.__getUncle(n)
        if n == self.root:
            n.isRed == False
        elif n.parent.isRed == True and u.isRed == True:
            self.__getUncle(n).isRed == False
            g = self.__getGrandparent(n)
            g.isRed = True
            n.parent.isRed = False
            u.isRed = False
            self.__fixUncleRed(g)

    def Search(self, key) -> Node:
        return self.__search(self.root, key)

    def __search(self, node, key) -> Any:
        if node == self.nil:
            return None
        if key > node.key:
            self.__search(node.right, key)
        elif key < node.key:
            self.__search(node.left, key)
        else:
            return node

    def __getGrandparent(self, node) -> Node:
        if node.parent != None:
            return node.parent.parent
        else:
            return None

    def __getUncle(self, node) -> Node:
        grandpa = self.__getGrandparent(node)
        if grandpa != None:
            if grandpa.left == node.parent:
                return grandpa.right
            else:
                return grandpa.left
        else:
            return None

    def __str__(self):
        print(
            "------------------------------------------------------------------------"
        )
        root = self.root
        print(root)
        childs = [root.left, root.right]
        print(root.left, root.right)
        while len(list(set(childs))) != 1:
            newChilds = []
            for child in childs:
                if child == self.nil:
                    continue
                for i in ["left", "right"]:
                    c = child.__getattribute__(i)
                    newChilds.append(c)
                    print(c, end=" ")
            childs = newChilds
            print()
        return (
            "------------------------------------------------------------------------"
        )

if __name__ == "__main__":
    tree = RedBlackTree(1)
    tree.Insert(2)
    tree.Insert(3)
    print(tree)

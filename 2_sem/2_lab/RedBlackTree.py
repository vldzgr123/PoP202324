from platform import node
from typing import Any


class Node:
    def __init__(self, key, isRed=True):
        self.key = key
        self.right = None
        self.left = None
        self.isRed = isRed
        self.parent = None

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ["right", "left"]:
            value.parent = self
            object.__setattr__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __str__(self) -> str:
        return f'({self.key} - {"RED" if self.isRed==True else "BLACK"})'


class RedBlackTree:
    def __init__(self, key):
        self.nil = Node(None, isRed=False)
        self.root = Node(key, isRed=False)
        self.right = self.nil
        self.left = self.nil

    def Insert(self, key):
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

    def __fixInsert(self, n):
        u = self.__getUncle(n)
        if n.parent.isRed == True:
            if u.isRed == True:
                self.__fixUncleRed(n)
            else:
                if n.parent.left == n:
                    self.__fixUncleBlackLeft(n.parent)
                else:
                    self.__fixUncleBlackRight(n)

    def __fixUncleBlackRight(self, n):
        self.__smallRotateRight(n)
        n.parent.isRed = False
        n.parent.right.isRed = True

    def __fixUncleBlackLeft(self, n):
        self.__smallRotateRight(n.parent)
        n.parent.isRed = False
        n.parent.right.isRed = True

    def __smallRotateRight(self, n):
        p = n.parent
        g = self.__getGrandparent(n)
        n.parent = g
        p.parent = n 
        if g.left == p.left: g.left = n
        else: g.right = n
        p.left = n.right  
        n.right = p.left 
        
    def __smallRotateLeft(self, n):
        p = n.parent
        g = self.__getGrandparent(n)
        n.parent = g
        p.parent = n 
        if g.left == p.left: g.left = n
        else: g.right = n
        p.left = n.right  
        n.right = p.left 
        
        

    def __fixUncleRed(self, n):
        u = self.__getUncle(n)
        if n.isRed == True and n == self.root:
            n.isRed == False
        elif n.parent.isRed == True and u.isRed == True:
            self.__getUncle(n).isRed == False
            g = self.__getGrandparent(n)
            g.isRed = True
            n.parent.isRed = False
            self.__fixUncleRed(g)

    def Search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        if node == self.nil:
            return None
        if key > node.key:
            self._search(node.right, key)
        elif key < node.key:
            self._search(node.left, key)
        else:
            return node

    def __getGrandparent(self, node):
        if node.parent != None:
            return node.parent.parent
        else:
            return None

    def __getUncle(self, node):
        grandpa = self.__getGrandparent(node)
        if grandpa != None:
            if grandpa.left == node.parent:
                return grandpa.right
            else:
                return grandpa.left
        else:
            return None

    def leftRotate(self, n):
        pivot = n.right
        pivot = n.parent
        if n.parent != None:
            if n.parent.left == n:
                n.parent.left = pivot
            else:
                n.parent.right = pivot

        n.right = pivot.left
        if pivot.left != None:
            pivot.left.parent = n

        n.parent = pivot
        pivot.left = n

    def rightRotate(self, n):
        pivot = n.left
        pivot = n.parent
        if n.parent != None:
            if n.parent.left == n:
                n.parent.left = pivot
            else:
                n.parent.right = pivot

        n.left = pivot.right
        if pivot.left != None:
            pivot.left.parent = n

        n.parent = pivot
        pivot.left = n

    # def __insertCase1(self, node):
    #     if node.parent == None:
    #         node.isRed = False
    #     else:
    #         self.__insertCase2(node)

    # def __insertCase2(self, node):
    #     if node.parent.isRed == False:
    #         return
    #     else:
    #         self.__insertCase3(node)

    # def __insertCase3(self, node):
    #     uncle = self.getUncle(node)

    #     if uncle != None and uncle.isRed == True:
    #         node.parent.isRed = False
    #         uncle.isRed = False
    #         grandparent = self.getGrandparent(node)
    #         grandparent.isRed = False
    #         self.__insertCase1(grandparent)
    #     else:
    #         self.__insertCase4(node)

    # def __insertCase4(self, node):
    #     grandparent = self.getGrandparent(node)

    #     if node == node.parent.right and node.parent == grandparent.left:
    #         self.leftRotate(node.parent)
    #         node = node.left
    #     elif node == node.parent.left and node.parent == grandparent.right:
    #         self.rightRotate(node.parent)
    #         node = node.right
    #     self.__insertCase5(node)

    # def __insertCase5(self, node):
    #     grandparent = self.getGrandparent(node)
    #     node.parent.isRed = False
    #     grandparent.isRed = True
    #     if node == node.parent.left and node.parent == grandparent.left:
    #         self.rightRotate(grandparent)
    #     else:
    #         self.leftRotate(grandparent)


if __name__ == "__main__"
    fir = Node(1)
    sec = Node(2)
    thr = Node(3)
    fir.right = sec
    print(sec.__dict__)
    print(fir.__dict__)

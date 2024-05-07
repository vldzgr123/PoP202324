from typing import Any


class Node:
    def __init__(self, key, isRed=True, right=None, left=None, parent=None) -> None:
        self.key = key
        self.right = right
        self.left = left
        self.isRed = isRed
        self.parent = parent

    def __str__(self):
        if self.parent != None and self.key != None:
            return f'({self.key} - {"RED" if self.isRed==True else "BLACK"} - PARENT {self.parent.key} - {"LEFT" if self.parent.left == self else "RIGHT"})'
        elif self.parent == None and self.key != None:
            return f'({self.key} - {"RED" if self.isRed==True else "BLACK"} - ROOT)'
        return f"(BLACK NIL)"


class RedBlackTree:
    def __init__(self) -> None:
        self.nil = Node(None, isRed=False)
        self.root = self.nil

    def Insert(self, key) -> Any:
        if self.__search(self.root, key) != None:
            return False
        newNode = Node(key)
        current = self.root
        parent = current
        if self.root == self.nil:
            self.root = Node(key, isRed=False)
            self.root.right = self.nil
            self.root.left = self.nil
            return True
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
                        self.__rotateRight(n.parent)
                        n.parent.isRed = False
                        n.parent.right.isRed = True
                    else:
                        self.__rotateLeft(n)
                        self.__rotateRight(n)
                        n.isRed = False
                        n.right.isRed = True
                else:
                    if n.parent.right == n:
                        self.__rotateLeft(n.parent)
                        n.parent.isRed = False
                        n.parent.left.isRed = True
                    else:
                        self.__rotateRight(n)
                        self.__rotateLeft(n)
                        n.isRed = False
                        n.left.isRed = True

    def __rotateRight(self, n):
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

    def __rotateLeft(self, n):
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
            n.isRed = False
            return
        if n.parent.isRed == True and u.isRed == True:
            self.__getUncle(n).isRed == False
            g = self.__getGrandparent(n)
            g.isRed = True
            n.parent.isRed = False
            u.isRed = False
            self.__fixUncleRed(g)

    def Search(self, key):
        return self.__search(self.root, key)

    def __search(self, n, key):
        if n == self.nil or n == None:
            return None
        if key > n.key:
            return self.__search(n.right, key)
        elif key < n.key:
            return self.__search(n.left, key)
        else:
            return n

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
        try:
            childs = [root.left, root.right]
            print(root.left, root.right)
        except:
            return "Tree empty!"
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

    def Erase(self, key) -> bool:
        n = self.__search(self.root, key)
        if n == None:
            return False
        p = n.parent
        if n.left == self.nil and n.right == self.nil:
            if n.isRed == True:
                self.__eraseZeroChild(n)
            else:
                if n.parent.isRed == True:
                    u = self.__getUncle(n)
                    self.__eraseZeroChild(n)
                    if self.root == self.nil: return True
                    elif (u.left != self.nil or u.right != self.nil) and (u.right.isRed == True or u.left.isRed == True):
                        self.__erasefixZeroChildBlackRedPNCF(u)
                    else:
                        u.isRed = True
                        u.parent.isRed = False
                else:
                    u = self.__getUncle(n)
                    if u.isRed == True:
                        if u.right. 
                self.__erasefixZeroChildBlack(n)
        elif (
            n.left != self.nil
            and n.right == self.nil
            or n.left == self.nil
            and n.right != self.nil
        ):
            self.__eraseOneChild(n)
        else:
            self.__eraseTwoChild(n)

        return True

    def Clear(self):
        self.root = self.nil
    
    # происходит относительно дяди удаляемого объекта    
    def __erasefixZeroChildBlackRedPNCF(self, n):
        if n.parent.left == n:
            if n.left != self.nil and n.right == self.nil:
                self.__rotateRight(n)
                n.isRed = True
                n.left.isRed = False
                n.right = True
            else:
                self.__rotateLeft(n.right)
                self.__rotateRight(n.parent)
                n.parent.right.isRed = False
        else:
            if n.left == self.nil and n.right != self.nil:
                self.__rotateLeft(n)
                n.isRed = True
                n.left.isRed = False
                n.left = True
            else:
                self.__rotateRight(n.left)
                self.__rotateLeft(n.parent)
                n.parent.left.isRed = False
            
    def __eraseZeroChild(self, n):
        if self.root == n:
            self.root = self.nil
        else:
            if n.parent.left == n:
                n.parent.left = self.nil
            else:
                n.parent.right = self.nil
            n = self.nil

    def __eraseOneChild(self, n):
        if self.root == n:
            if n.left != self.nil:
                self.root = n.left
            else:
                self.root = n.right
        else:
            tmp = n
            p = n.parent
            if n.left != self.nil:
                tmp = n.left
            else:
                tmp = n.right
            if p.left == n:
                p.left = tmp
            else:
                p.right = tmp
            tmp.parent = p
            tmp.isRed = False
            n.parent = None
            n.left = None
            n.right = None

    def __eraseTwoChild(self, n):
        maxNode = self.__searchMax(n.left)
        if n == self.root:
            maxNode.parent.right = self.nil
            maxNode.parent = None
            n.left.parent = maxNode
            maxNode.left = n.left
            n.left = None
            n.parent = None
        else:
            maxNode.parent.right = self.nil
            maxNode.parent = n.parent
            if n.parent.left == n:
                n.parent.left = maxNode
            else:
                n.parent.right = maxNode
            n.left.parent = maxNode
            maxNode.left = n.left
            n.left = None
            n.parent = None
        self.Erase(maxNode)
    
    def __searchMax(self, n) -> Any:
        if n==None or n == self.nil: return None
        current = n
        while True:
            if current.left == self.nil: return current
            else: current = current.left

    def 

if __name__ == "__main__":
    tree = RedBlackTree()
    tree.Insert(0)
    tree.Insert(1)
    tree.Insert(3)
    tree.Insert(2)
    print(tree)
    tree.Erase(2)
    print(tree)

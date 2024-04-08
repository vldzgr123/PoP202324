class Node:
    def __init__(self, key, isRed=True):
        self.key = key
        self.name = key
        self.right = None
        self.left = None
        self.isRed = isRed
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, isRed=False)
        self.root = Node(None)
        self.right = self.nil
        self.left = self.nil

    def Insert(self, key):
        newNode = Node(key)
        current = self.root
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

    def getGrandparent(self, node):
        if node != None and node.parent != None:
            return node.parent.parent
        else:
            return None

    def getUncle(self, node):
        grandNode = self.getGrandparent(node)
        if grandNode != None:
            if grandNode.left == node.parent:
                return grandNode.right
            else:
                return grandNode.left
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

    # Текущий узел N в корне дерева. В этом случае, он перекрашивается в чёрный цвет, чтобы оставить верным Свойство 2 (Корень — чёрный).
    # Так как это действие добавляет один чёрный узел в каждый путь, Свойство 5 (Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов) не нарушается.
    def insertCase1(self, node):
        if node.parent == None:
            node.isRed = False
        else:
            self.insertCase2(node)

    def insertCase2(self, node):
        if node.parent.isRed == False:
            return
        else:
            self.insertCase3(node)

    def insertCase3(self, node):
        uncle = self.getUncle(node)

        if uncle != None and uncle.isRed == True:
            node.parent.isRed = False
            uncle.isRed = False
            grandparent = self.getGrandparent(node)
            grandparent.isRed = False
            self.insertCase1(grandparent)
        else:
            self.insertCase4(node)

    def insertCase4(self, node):
        grandparent = self.getGrandparent(node)
        
        if node == node.parent.right and node.parent == grandparent.left:
            self.leftRotate(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == grandparent.right:
            self.rightRotate(node.parent)
            node=node.right
        self.insertCase5(node)
    
    def insertCase5(self,node):
        grandparent = self.getGrandparent(node)
        node.parent.isRed = False
        grandparent.isRed = True
        if node == node.parent.left and node.parent == grandparent.left:
            self.rightRotate(grandparent)
        else:
            self.leftRotate(grandparent)
            
    
        
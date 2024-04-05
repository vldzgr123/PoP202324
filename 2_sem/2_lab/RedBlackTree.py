class Node:
    def __init__(self, key):
        self.key = key
        self.name = key
        self.right = None
        self.left = None
        self.isRed = True

    def _getGrandPa(self):
        if self.key != None and self.parent != None:
            return self.parent.parent
        else:
            return None

    def _getUncle(self):
        grandParent = self._getGrandPa()
        if grandParent == None:
            return None
        if self.parent == grandParent.left:
            return grandParent.right
        else:
            return grandParent.left


class RedBlackTree:
    def __init__(self):
        self.root = Node(None)
        self.root.isRed = False

    def Insert(self, key):
        newNode = Node(key)
        current = self.root
        parent = current
        while current.key != None:
            parent = current
            if newNode.key < current.key:
                current = current.left
            else:
                current = current.right
        newNode.parent = parent
        if parent.key < newNode.key:
            parent.left = newNode
        else:
            parent.right = newNode
        self._balanceInsert(newNode)

    def _getGrandPa(self, node):
        if node != None and node.parent != None:
            return node.parent.parent
        else:
            return None

    def _getUncle(self, node):
        grandParent = self._getGrandPa(node)
        if grandParent == None:
            return None
        if node.parent == grandParent.left:
            return grandParent.right
        else:
            return grandParent.left

    def _rotateRight(self, node):

        pivot = node.left

        pivot.parent = node.parent
        if node.parent != None:
            if node.parent.left == node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot

        node.right = pivot.left
        if pivot.left != None:
            pivot.left.parent = node

        node.parent = pivot
        pivot.left = node

class Node:
    def __init__(self, key):
        self.key = key
        self.name = key
        self.right = None
        self.left = None
        self.isRed = False


class RedBlackTree:
    def __init__(self, key):
        rootNode = Node(key)
        self.root = rootNode

    def Insert(self, key):
        node = Node(key)
        self._InsertNode(self.root, node)

    def _InsertNode(self, parent, node):
        if parent.key > node.key:
            if parent.right is None:
                if parent.isRed == False:
                    node.isRed = True
                else:
                    node.isRed = False
                parent.right = node
            else:
                self._InsertNode(parent.right, node)
        else:
            if parent.left is None:
                if parent.isRed == False:
                    node.isRed = True
                else:
                    node.isRed = False
                parent.left = node
            else:
                self._InsertNode(parent.left, node)

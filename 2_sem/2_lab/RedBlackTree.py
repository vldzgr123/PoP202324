class Node:
    def __init__(self, key, isRed=False):
        self.key = key 
        self.right = None
        self.left = None
        self.isRed = isRed
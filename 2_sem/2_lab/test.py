class Node:
    def __init__(self, key, isRed=True):
        self.key = key
        self.right = None
        self.left = None
        self.isRed = isRed
        self.parent = None

    def __str__(self) -> str:
        return f'({self.key} {"RED" if self.isRed==True else "BLACK"})'


fir = Node(12)
sec = Node(12)
th = Node(12)
nil = Node(None, isRed=False)
fir.left = sec
fir.right = th
fir.right.isRed = False

print(th)

"""

Q - Count frequency of words in a sentence


STEPS


1 - 




"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def inorder(root):
        if root:
            inorder(root.left)
            print(root.data, end=" ")
            inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

inorder(root)
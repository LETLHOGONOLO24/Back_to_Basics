"""

Q - Simple binary tree with traversal


STEPS


1 - self.data stores the value
    self.left is a pointer to left child
    self.right is a pointer to right child

2 - if root checks if node exists
    inorder(root.left) visits left subtree
    print(root.data, end="") process current node
    inorder(root.right) visits right subtree

    inorder = left -> root -> right is a recursive pattern that follows
    the pattern (2, 1, 3)

3 - root = Node(1) creates root node with value 1
    root.left = Node(2) creates left child with value 2
    root.right = Node(3) creates right child with value 3




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
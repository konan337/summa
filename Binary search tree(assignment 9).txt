# lab assignment 9
# Implement operations on Binary Search Tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Main Program
root = None
keys = [50, 30, 70, 20, 40, 60, 80]
for k in keys:
    root = insert(root, k)

print("Inorder Traversal:")
inorder(root)
print("\nSearch for 40:", "Found" if search(root, 40) else "Not Found")

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Створення дерева
# Test
root = AVLNode(5)
root.left = AVLNode(3)
root.right = AVLNode(7)
root.left.left = AVLNode(2)
root.left.right = AVLNode(4)
root.right.left = AVLNode(6)
root.right.right = AVLNode(8)

print("Мінімальне значення в AVL-дереві:", min_value_node(root).key)
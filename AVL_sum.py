class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def sum_of_avl_tree(node):
    if node is None:
        return 0
    return node.key + sum_of_avl_tree(node.left) + sum_of_avl_tree(node.right)


# Приклад використання
root = AVLNode(10)
root.left = AVLNode(5)
root.right = AVLNode(15)
root.left.left = AVLNode(3)
root.left.right = AVLNode(7)
root.right.right = AVLNode(18)

total_sum = sum_of_avl_tree(root)
print("Сума всіх значень в AVL-дереві:", total_sum)
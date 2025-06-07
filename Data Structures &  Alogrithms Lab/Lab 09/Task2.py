class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def construct_from_traversals(self, in_order, pre_order):
        if not in_order or not pre_order:
            return None

        root_value = pre_order.pop(0)
        root = BSTNode(root_value)

        inorder_index = in_order.index(root_value)

        root.left = self.construct_from_traversals(in_order[:inorder_index], pre_order)
        root.right = self.construct_from_traversals(in_order[inorder_index + 1:], pre_order)

        return root

    def display_in_order(self):
        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                print(node.value, end=" ")
                in_order_traversal(node.right)
        in_order_traversal(self.root)
        print()

    def display_post_order(self):
        def post_order_traversal(node):
            if node:
                post_order_traversal(node.left)
                post_order_traversal(node.right)
                print(node.value, end=" ")
        post_order_traversal(self.root)
        print()
# Example 1 usage:
bst = BinarySearchTree()
in_order = ['D', 'B', 'E', 'A', 'F', 'C']
pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
bst.root = bst.construct_from_traversals(in_order, pre_order)
# Verify constructed tree
print("In-order traversal of constructed BST:")
bst.display_in_order()
print("Post-order traversal of constructed BST:")
bst.display_post_order()

# Example 2 usage:
bst2 = BinarySearchTree()
in_order = [5, 10, 15, 25, 27, 30, 35, 40, 45, 50, 52, 55, 60, 65, 70, 75, 80, 85, 90, 100]
pre_order = [50, 25, 10, 5, 15, 40, 30, 27, 35, 45, 75, 60, 55, 52, 65, 70, 90, 80, 85, 100]
bst2.root = bst2.construct_from_traversals(in_order, pre_order)
# Verify constructed tree
print("In-order traversal of constructed BST:")
bst2.display_in_order()
print("Post-order traversal of constructed BST:")
bst2.display_post_order()


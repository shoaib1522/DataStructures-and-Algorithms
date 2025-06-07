class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_element_root(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self.root.set_value(element)

    def insert_left_child(self, parent_value, child_value):
        parent = self.find_node(self.root, parent_value)
        if parent:
            parent.set_left(Node(child_value))

    def insert_right_child(self, parent_value, child_value):
        parent = self.find_node(self.root, parent_value)
        if parent:
            parent.set_right(Node(child_value))

    def delete_element(self, element):
        self.root = self._delete_recursive(self.root, element)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.get_value():
            node.left = self._delete_recursive(node.left, key)
        elif key > node.get_value():
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.set_value(min_larger_node.get_value())
            node.right = self._delete_recursive(node.right, min_larger_node.get_value())

        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_node(self, node, value):
        if node is None:
            return None
        if node.get_value() == value:
            return node
        left_result = self.find_node(node.get_left(), value)
        if left_result:
            return left_result
        return self.find_node(node.get_right(), value)

    def display_pre_order(self, node):
        if node:
            print(node.get_value(), end=' ')
            self.display_pre_order(node.get_left())
            self.display_pre_order(node.get_right())

    def display_in_order(self, node):
        if node:
            self.display_in_order(node.get_left())
            print(node.get_value(), end=' ')
            self.display_in_order(node.get_right())

    def display_post_order(self, node):
        if node:
            self.display_post_order(node.get_left())
            self.display_post_order(node.get_right())
            print(node.get_value(), end=' ')

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.get_left()) + self._count_nodes_recursive(node.get_right())

    def min_value(self, node):
        if node is None:
            return None
        while node.get_left() is not None:
            node = node.get_left()
        return node.get_value()

    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.get_left() is None and node.get_right() is None:
            return 1
        return self.count_leaf_nodes(node.get_left()) + self.count_leaf_nodes(node.get_right())

    def non_rec_pre_order(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.get_value(), end=' ')
            if node.get_right():
                stack.append(node.get_right())
            if node.get_left():
                stack.append(node.get_left())

    def non_rec_in_order(self):
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.get_left()
            current = stack.pop()
            print(current.get_value(), end=' ')
            current = current.get_right()

    def non_rec_post_order(self):
        if self.root is None:
            return
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.get_left():
                stack1.append(node.get_left())
            if node.get_right():
                stack1.append(node.get_right())
        while stack2:
            node = stack2.pop()
            print(node.get_value(), end=' ')

    def find_balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.get_left()) - self._height(node.get_right())

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.get_left()), self._height(node.get_right())) + 1

    def display_ancestors(self, node_data):
        if self.root is None:
            return False
        return self._display_ancestors_helper(self.root, node_data)

    def _display_ancestors_helper(self, node, node_data):
        if node is None:
            return False
        if node.get_value() == node_data:
            return True
        if (self._display_ancestors_helper(node.get_left(), node_data) or
                self._display_ancestors_helper(node.get_right(), node_data)):
            print(node.get_value(), end=' ')
            return True
        return False

    def display_descendants(self, node_data):
        target = self.find_node(self.root, node_data)
        if target:
            self.display_pre_order(target)

    def height_of_tree(self):
        return self._height(self.root)


# Example Usage:
bt = BinaryTree()
bt.insert_element_root(10)
bt.insert_left_child(10, 5)
bt.insert_right_child(10, 15)
bt.insert_left_child(5, 2)
bt.insert_right_child(5, 7)

print("Pre-order Traversal:")
bt.display_pre_order(bt.root)  # Output: 10 5 2 7 15

print("\nIn-order Traversal:")
bt.display_in_order(bt.root)  # Output: 2 5 7 10 15

print("\nPost-order Traversal:")
bt.display_post_order(bt.root)  # Output: 2 7 5 15 10

print("\nCount of Nodes:")
print(bt.count_nodes())  # Output: 5

bt.delete_element(5)
print("\nIn-order Traversal after deleting 5:")
bt.display_in_order(bt.root)  # Output: 2 7 10 15

print("\nMinimum Value in the Tree:")
print(bt.min_value(bt.root))  # Output: 2

print("\nCount of Leaf Nodes:")
print(bt.count_leaf_nodes(bt.root))  # Output: 3

print("\nNon-Recursive Pre-order Traversal:")
bt.non_rec_pre_order()  # Output: 10 2 7 15

print("\nNon-Recursive In-order Traversal:")
bt.non_rec_in_order()  # Output

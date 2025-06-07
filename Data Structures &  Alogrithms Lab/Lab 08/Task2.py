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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_element(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        temp = self.root
        while True:
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                return 

    def delete_element(self, value):
        if self.root is None:
            return

        parent = None
        temp = self.root
        while temp:
            if value == temp.value:
                if temp.left is None and temp.right is None:
                    if parent:
                        if parent.left == temp:
                            parent.left= None
                        else:
                            parent.right = None
                    else:
                        self.root = None
                elif temp.left is None:
                    if parent:
                        if parent.left == temp:
                            parent.left= temp.right
                        else:
                            parent.right =temp.right
                    else:
                        self.root = temp.right
                elif temp.right is None:
                    if parent:
                        if parent.left==temp:
                            parent.left = temp.left
                        else:
                            parent.right = temp.left
                    else:
                        self.root = temp.left
                else:
                    successor_parent=temp
                    successor = temp.right
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left
                    if successor_parent != temp:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                    temp.value = successor.value
                return
            elif value < temp.value:
                parent = temp
                temp = temp.left
            else:
                parent = temp
                temp = temp.right

    def display_pre_order(self):
        if self.root is None:
            return

        stack = [self.root]
        while stack:
            temp = stack.pop()
            print(temp.value, end=" ")
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

    def display_in_order(self):
        if self.root is None:
            return

        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            if not stack:
                break
            temp = stack.pop()
            print(temp.value, end=" ")
            temp = temp.right

    def display_post_order(self):
        if self.root is None:
            return

        stack1 = [self.root]
        stack2 = []
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)
        while stack2:
            print(stack2.pop().value, end=" ")

    def total_elements(self):
        if self.root is None:
            return 0
        count = 0
        stack = [self.root]
        while stack:
            temp = stack.pop()
            count += 1
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return count


# Example usage:
bst = BinarySearchTree()
bst.insert_element(10)
bst.insert_element(5)
bst.insert_element(15)
bst.insert_element(3)
bst.insert_element(7)
bst.insert_element(12)
bst.insert_element(20)

print("PreOrder Traversal:")
bst.display_pre_order()
print("\nInOrder Traversal:")
bst.display_in_order()
print("\nPostOrder Traversal:")
bst.display_post_order()

print("\nTotal Elements:", bst.total_elements())

# Deleting an element
bst.delete_element(15)
print("\nAfter deleting 15:")
print("InOrder Traversal:")
bst.display_in_order()

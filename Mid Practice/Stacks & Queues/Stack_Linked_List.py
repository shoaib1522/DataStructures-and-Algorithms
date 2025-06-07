class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.isEmpty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            print("Stack is empty")
            return None

    def top_Func(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print("Stack is empty")
            return None

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.top is None


stack = Stack()
print("Is stack empty?", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top_Func())
print("Popping:", stack.pop())
print("Top element after popping:", stack.top_Func())
print("Is stack empty?", stack.isEmpty())
print("Size of stack:", stack.size())

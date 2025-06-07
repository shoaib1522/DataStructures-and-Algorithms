class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.size = 0

    def push(self, item):
        if self.size == self.capacity:
            self._resize()
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_item = self.stack[self.size - 1]
        self.stack[self.size - 1] = None
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def _resize(self):
        self.capacity *= 2
        new_stack = [None] * self.capacity
        for i in range(self.size):
            new_stack[i] = self.stack[i]
        self.stack = new_stack

    def stack_size(self):
        return self.size

# Example usage
stack = ArrayStack()
print("Is stack empty?", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())
print("Popping:", stack.pop())
print("Top element after popping:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Size of stack:", stack.stack_size())

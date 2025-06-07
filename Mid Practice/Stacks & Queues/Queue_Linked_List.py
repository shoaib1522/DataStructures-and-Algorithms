class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front_node.data
            if self.front_node == self.rear_node:
                self.front_node = None
                self.rear_node = None
            else:
                self.front_node = self.front_node.next
            return dequeued_item
        else:
            print("Queue is empty")
            return None

    def front(self):
        if not self.is_empty():
            return self.front_node.data
        else:
            print("Queue is empty")
            return None

    def size(self):
        current = self.front_node
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.front_node is None

# Example usage
queue = Queue()
print("Is queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.front())
print("Dequeuing:", queue.dequeue())
print("Front element after dequeuing:", queue.front())
print("Is queue empty?", queue.is_empty())
print("Size of queue:", queue.size())

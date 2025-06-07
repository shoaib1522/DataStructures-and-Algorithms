class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enQueue(self, process):
        if self.isFull():
            print("Queue is full")
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = process

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

class CircularQueue():
    def __init__(self, size): 
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    def isEmpty(self):
        if self.queue[0]!=None:
            return False
        return True
        
    def isFull(self):
        for i in range((self.size)):
            if self.queue[i]==None:
                return False
        return True
    def display(self):
        for i in range(self.size):
            if self.queue[i]!=None:
                print(self.queue[i], end=" ")
    def enqueue(self,data):
        if self.isFull():
            print('The Circular Queue is Full')
            return
        elif self.isEmpty():
            self.rear= 0
            self.front = 0
        else:
            self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=data
    def dequeue(self):
        if self.isEmpty():
             return False
        data = self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        return data
if __name__ == "__main__": 
    ob = CircularQueue(5) 
    ob.enqueue(14) 
    ob.enqueue(22) 
    ob.enqueue(13) 
    ob.enqueue(-6) 
    ob.display() 
    print("\nDeleted value = ", ob.dequeue()) 
    ob.enqueue(-6)
    ob.display() 
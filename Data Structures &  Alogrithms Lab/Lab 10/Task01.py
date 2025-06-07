import math
class Student: 
    def __init__(self, rollNo, cgpa): 
        self.rollNo = rollNo 
        self.cgpa = cgpa 
class StudentMaxHeap: 
    def __init__(self, size): 
        self.maxSize = size   # Maximum number of students that can be stored in the heap 
        self.currSize = 0     # Current number of students present in the heap 
        self.student = [None] * size  # Array of students which will be arranged like a Max Heap 
 
    def isEmpty(self):  # Checks whether the heap is empty or not 
        return self.currSize == 0 
 
    def isFull(self):  #Checks whether the heap is full or not 
        return self.currSize == self.maxSize 
 
    def insert(self, student): 
        if self.isFull():
            return False
        self.student[self.currSize] = student
        self.currSize += 1
        self._heapify_up(self.currSize - 1)
        return True
    def removeBestStudent(self): 
        if self.isEmpty():	
            return None
        bestStudent = self.student[0]
        self.student[0] = self.student[self.currSize - 1]
        self.student[self.currSize - 1] = None
        self.currSize -= 1
        self._heapify_down(0)
        return bestStudent
    def levelOrder(self): 
        for i in range(self.currSize):
            print(f"Roll No: {self.student[i].rollNo}, CGPA: {self.student[i].cgpa}")
    def _heapify_up(self, index): 
        parent = (index - 1) // 2
        if index > 0 and self.student[index].cgpa > self.student[parent].cgpa:
            self.student[index], self.student[parent] = self.student[parent], self.student[index]
            self._heapify_up(parent)
    def height(self):
        return math.ceil(math.log(self.currSize+1))
    def _heapify_down(self, index):
        l = 2 * index + 1
        r = 2 * index + 2
        largest = index
        if l < self.currSize and self.student[l].cgpa > self.student[largest].cgpa:
            largest = l
        if r < self.currSize and self.student[r].cgpa > self.student[largest].cgpa:
            largest = r
        if largest != index:
            self.student[index], self.student[largest] = self.student[largest], self.student[index]
            self._heapify_down(largest)
heap = StudentMaxHeap(10) 
heap.insert(Student(1, 3.8)) 
heap.insert(Student(2, 3.9)) 
heap.insert(Student(3, 3.7)) 
heap.insert(Student(4, 4.0)) 
heap.levelOrder() 
 
 
s = heap.removeBestStudent() 
print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}") 
 
s = heap.removeBestStudent() 
print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}") 
 
heap.levelOrder() 
print(f"Height of the heap: {heap.height()}") 
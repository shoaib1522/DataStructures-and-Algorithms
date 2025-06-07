class MinHeap:
    def __init__(self, cap=10):
        self.heap_size = 0
        self.capacity = cap
        self.array = [0] * cap

    def swap(self, x, y):
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.array[l] < self.array[i]:
            smallest = l
        if r < self.heap_size and self.array[r] < self.array[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def extract_min(self):
        if self.heap_size <= 0:
            return float('inf')
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.array[0]

        root = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify(0)

        return root

    def decrease_key(self, i, new_val):
        self.array[i] = new_val
        while i != 0 and self.array[self.parent(i)] > self.array[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def get_min(self):
        return self.array[0]

    def delete_key(self, i):
        self.decrease_key(i, float('-inf'))
        return self.extract_min()

    def insert_key(self, k):
        if self.heap_size == self.capacity:
            print("\nOverflow: Could not insertKey")
            return

        self.heap_size += 1
        i = self.heap_size - 1
        self.array[i] = k

        while i != 0 and self.array[self.parent(i)] > self.array[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
def maxProduct(nums):
    heap = MinHeap(len(nums)) 
    for num in nums:
        heap.insert_key(num)
        if heap.heap_size > 2:
            heap.extract_min()
    first = heap.extract_min()
    second = heap.extract_min()

    return (first - 1) * (second - 1)
def frequencySort(s):
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    heap = MinHeap(len(freq_map))
    for char, freq in freq_map.items():
        heap.insert_key((-freq, char))
    sorted_string = []
    while heap.heap_size > 0:
        freq, char = heap.extract_min()
        sorted_string.append(char * -freq)
    string=""
    for s in sorted_string:
        string+=s
    return string 
print(frequencySort("tree"))    
print(frequencySort("cccaaa"))  
print(frequencySort("Aabb"))    
# print(maxProduct([3, 4, 5, 2]))  
# print(maxProduct([1, 5, 4, 5]))  
# print(maxProduct([3, 7]))        
# if __name__ == "__main__":
#     h = MinHeap(11)

#     h.insert_key(3)
#     h.insert_key(2)
#     h.insert_key(15)
#     h.insert_key(5)
#     h.insert_key(4)
#     h.insert_key(45)

#     print("Extracting Data From Min Heap")
#     x = h.extract_min()
#     while x != float('inf'):
#         print(x, end=' ')
#         x = h.extract_min()
#     print()

#     # inserting elements again
#     h.insert_key(3)
#     h.insert_key(2)
#     h.insert_key(15)
#     h.insert_key(5)
#     h.insert_key(4)
#     h.insert_key(45)

#     print("Extract Min:", h.extract_min())
#     print("Get Min:", h.get_min())

#     h.delete_key(0)
#     print("Get Min After Deleting 0:", h.get_min())
#     h.decrease_key(4, 1)
#     print("Get Min After Decreasing the Key at index 4 to 1:", h.get_min())

#     print("Extracting Data Again From Min Heap")
#     x = h.extract_min()
#     while x != float('inf'):
#         print(x, end=' ')
#         x = h.extract_min()
#     print()

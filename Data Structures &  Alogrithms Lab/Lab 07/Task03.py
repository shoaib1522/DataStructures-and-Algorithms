import random 
def getRandomNumber(start, end): 
    return random.randint(start, end)
class HashTable:
    def __init__(self, size):
        self.table = [None] * size  # Dynamic array to store integers
        self.S = size  # Total number of slots in the table
        self.n = 0  # Current number of elements present in the table

    def getHashValue(self, number):
        x=  number % self.S
        return x
    def inserting(self,number):
        value = self.getHashValue(number)%self.S
        if self.table[value]==None:
            self.table[value]=number
            self.n+=1
            return True
        else:
            return False
    def elements_count(self):
        count=0
        for i in range(self.S):
            if self.table[i]!=None:
                count+=1
        return count
    def reset(self):
        self.table = [None] * self.S # Dynamic array to store integers
        self.S = 0 # Total number of slots in the table
        self.n = 0  
def main():
    array= []
    for i in range(3):
        A=True
        capacity=random.randint(5,50)
        HashTablee= HashTable(capacity)
        j=1
        while A and j<=50:
            capacity=random.randint(5,50)
            HashTablee= HashTable(capacity)
            x = getRandomNumber(1,100)
            if HashTablee.inserting(x):
                A= True
                j+=1
            else:
                A=False
            count= HashTablee.elements_count()
            array.append(count)
            HashTablee.reset()
        numbers=0
        for i in range(len(array)):
            numbers+=int(array[i])
        print("Average Number of elements inserted are: ", numbers/20)
main()
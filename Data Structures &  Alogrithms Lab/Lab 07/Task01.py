class HashTable: 
    def __init__(self, size): 
        self.table = [None] * size  # Dynamic array of strings to store 
        self.S = size  # Total number of slots in the table 
        self.n = 0  # Current number of elements present in the table 
 
    def __del__(self):
            self.S=None
            self.n=None
            del self.table
            return
    def isEmpty(self): 
        if self.n==0:
            return True
        return False
    def isFull(self): 
        if self.n== self.S:
            return True
        return False
    def loadFactor(self): 
        x = self.n / self.S
        return x
    def getHashValue(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp
    def insert(self, name) :
        i = self.getHashValue(name) % self.S
        if self.table[i] == None:
            self.table[i]=name
            self.n +=1
            return True
        elif self.table[i]!=None:
            j = 1
            while True:
                if self.table[(i + j) % self.S] !=None:
                    j += 1
                else:
                    break
            self.table[(j + i)% self.S]=name
            self.n += 1
            return True
        return False
    def search(self, name):
        value = self.getHashValue(name)% self.S
        if self.table[value]==name:
            return True
        elif self.table[value]!=name:
            j=1
            while True:
                if self.table[j+value]==name:
                    return True
                else:
                    if j!=self.S:
                        j+=1
                    if j==self.S:
                        break
        return False
    def display(self):
        for i in range(self.S):
            if self.table[i]==None:
                print(f"{i}-Empty")
            else:
                print(f"{i}-{self.table[i]}")
    def remove(self, name):
        value= self.getHashValue(name)%self.S
        if self.table[value]==name:
            self.table[value]=None
            return True
        elif self.table[value]!=name:
            j=1
            while True:
                if self.table[j+value]==name:
                    self.table[j+value]=None
                    return True
                else:
                    if j!=self.S:
                        j+=1
                    if j==self.S:
                        break
        return False
def main():
    size = int(input("Enter the size of Hash Table: "))
    hash_table = HashTable(size)
    while True:
        print("\n1. Insert a name")
        print("2. Search for a name")
        print("3. Remove a name")
        print("4. Display the Hash Table")
        print("5. Display Load Factor of the table")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name to insert: ")
            if hash_table.insert(name):
                print("Name inserted successfully.")
            else:
                print("Failed to insert name.")
        elif choice == 2:
            name = input("Enter the name to search: ")
            if hash_table.search(name):
                print("Name found.")
            else:
                print("Name not found.")
        elif choice == 3:
            name = input("Enter the name to remove: ")
            if hash_table.remove(name):
                print("Name removed successfully.")
            else:
                print("Name not found.")
        elif choice == 4:
            hash_table.display()
        elif choice == 5:
            print("Load Factor:", hash_table.loadFactor())
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
main()
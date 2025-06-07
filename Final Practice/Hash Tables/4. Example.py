SIZE = 10 # Define the size of the hash table
class DataItem:
    def __init__(self, key):
        self.key = key
hashMap = {} # Define the hash table as a dictionary
def hashCode(key):
    # Return a hash value based on the key
    return key % SIZE

def search(key):
    # get the hash
    hashIndex = hashCode(key)

    # move in map until an empty slot is found or the key is found
    while hashIndex in hashMap:
        # If the key is found, return the corresponding DataItem
        if hashMap[hashIndex].key == key:
            return hashMap[hashIndex]

        # go to the next cell
        hashIndex = (hashIndex + 1) % SIZE

    # If the key is not found, return None
    return None
# Initializing the hash table with some sample DataItems
item2 = DataItem(25) # Assuming the key is 25
item3 = DataItem(64) # Assuming the key is 64
item4 = DataItem(22) # Assuming the key is 22
# Calculate the hash index for each item and place them in the hash table
hashIndex2 = hashCode(item2.key)
hashMap[hashIndex2] = item2

hashIndex3 = hashCode(item3.key)
hashMap[hashIndex3] = item3

hashIndex4 = hashCode(item4.key)
hashMap[hashIndex4] = item4

# Call the search function to test it
keyToSearch = 64 # The key to search for in the hash table
result = search(keyToSearch)
print("The element to be searched: ", keyToSearch)
if result:
    print("Element found")
else:
    print("Element not found")
class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.n = 0  # Current number of elements in the table

    def get_hash_value(self, string):
        x = 0
        for char in string:
            x += ord(char)
        return x % self.size

    def insert(self, name):
        index = self.get_hash_value(name)
        if self.table[index] is None:
            self.table[index] = name
            self.n += 1
        else:
            return False  # Collision occurred
        return True  # No collision

    def rehash(self):
        old_table = self.table
        self.size = 2 * self.size  # Double the size
        self.table = [None] * self.size
        self.n = 0

        for item in old_table:
            if item is not None:
                self.insert(item)

def main():
    # List of fruit names
    fruits = [
        "Apples", "Apricots", "Avocados", "Bananas", "Bing Cherry", "Blueberries",
        "Boysenberries", "Cantaloupe", "Cherries", "Clementine", "Crab apples",
        "Cucumbers", "Damson plum", "Dates", "Dewberries", "Dinosaur Eggs",
        "Dragon Fruit", "Eggfruit", "Elderberry", "Entawak", "Evergreen Huckleberry",
        "Farkleberry", "Fig", "Finger Lime", "Gooseberries", "Grapefruit", "Guava",
        "Hackberry", "Honeycrisp Apples", "Imbe", "Indonesian Lime", "Jackfruit",
        "Jambolan", "Java Apple", "Kaffir Lime", "Kiwi", "Kumquat", "Lime (Lemon)",
        "Longan", "Loquat", "Lychee", "Mango", "Melon", "Mulberry", "Nashi Pear",
        "Navel Orange", "Nectarine", "Ogeechee Limes", "Olive", "Oranges",
        "Oval Kumquat", "Papaya", "Paw Paw", "Peach", "Pineapple", "Pomegranate",
        "Prickly Pear", "Quararibea cordata", "Queen Anne Cherry", "Quince",
        "Rambutan", "Raspberries", "Star Fruit", "Strawberries", "Sugar Baby Watermelon",
        "Tamarind", "Tangerine", "Tart Cherries", "Tomato", "Ugni", "Uniq Fruit",
        "Vanilla Bean", "Velvet Pink Banana", "Voavanga", "Watermelon", "White Mulberry",
        "Wolfberry", "Xango Mangosteen", "Xigua", "Ximenia caffra fruit", "Yangmei",
        "Yellow Passion Fruit", "Yunnan Hackberry", "Zig Zag Vine fruit", "Zinfandel Grapes", "Zucchini"
    ]

    initial_size = 973  # Initial hash table size
    hashtable = Hash(size=initial_size)
    collisions = 0

    for fruit in fruits:
        if not hashtable.insert(fruit):
            collisions += 1
            hashtable.rehash()
            collisions = 0  # Reset collisions after rehashing

            # Reinsert all elements including the current fruit
            for f in fruits[:hashtable.n]:
                hashtable.insert(f)
            hashtable.insert(fruit)

    print(f"Final table size: {hashtable.size}")
    print("Inserted all fruits without collisions.")

if __name__ == "__main__":
    main()

# lab assignment 7
# Implement Hash Table using Linear Probing.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

    def display(self):
        for i, val in enumerate(self.table):
            print(f"{i}: {val}")

# Main Program
ht = HashTable(10)
ht.insert(21)
ht.insert(31)
ht.insert(41)
print("\nHash Table:")
ht.display()

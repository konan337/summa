# lab assignment 6
# Implement Hash Table using Chaining.

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        self.table[index].append((key, value))

    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")

# Main Program
ht = HashTable()
ht.insert(11, "Amit")
ht.insert(21, "Raj")
ht.insert(31, "Kiran")
print("\nHash Table:")
ht.display()

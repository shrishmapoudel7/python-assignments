class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

# Example usage:
hash_table = HashTable(10)
hash_table.insert("app", 10)
hash_table.insert("bull", 20)
hash_table.insert("oreo", 30)

print(hash_table.search("app"))  
print(hash_table.search("bull"))  
print(hash_table.search("oreo"))  
print(hash_table.search("green"))  

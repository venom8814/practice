class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        """Визуализация таблицы"""
        print("\n=== Состояние хэш-таблицы ===")
        for i, chain in enumerate(self.table):
            print(f"[{i}]: {chain}")
        print("=============================")


if __name__ == "__main__":
    ht = HashTable(5)

    ht.put("apple", 1)
    ht.put("banana", 2)
    ht.put("cherry", 3)
    ht.put("date", 4)
    ht.put("elderberry", 5)
    ht.put("apple", 99)

    ht.display()

    print("Значение 'apple':", ht.get("apple"))
    print("Удалено 'banana':", ht.remove("banana"))
    ht.display()
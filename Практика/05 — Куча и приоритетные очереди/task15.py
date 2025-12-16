class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._sift_down(0)
        return min_val

    def build_heap(self, arr):
        self.heap = arr[:]
        start = len(self.heap) // 2 - 1
        for i in range(start, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _sift_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._sift_down(smallest)

    def is_valid_heap(self):
        """Проверяет, что куча удовлетворяет свойству мин-кучи"""
        for i in range(len(self.heap)):
            left = self.left_child(i)
            right = self.right_child(i)
            if left < len(self.heap) and self.heap[left] < self.heap[i]:
                return False
            if right < len(self.heap) and self.heap[right] < self.heap[i]:
                return False
        return True

    def __str__(self):
        return str(self.heap)


print("=== ЗАДАНИЕ 15: БИНАРНАЯ МИН-КУЧА ===")

heap = MinHeap()

print("\nВставка элементов: 5, 3, 8, 1, 7")
heap.insert(5)
print(f"Куча после вставки 5: {heap} | Валидна: {heap.is_valid_heap()}")

heap.insert(3)
print(f"Куча после вставки 3: {heap} | Валидна: {heap.is_valid_heap()}")

heap.insert(8)
print(f"Куча после вставки 8: {heap} | Валидна: {heap.is_valid_heap()}")

heap.insert(1)
print(f"Куча после вставки 1: {heap} | Валидна: {heap.is_valid_heap()}")

heap.insert(7)
print(f"Куча после вставки 7: {heap} | Валидна: {heap.is_valid_heap()}")

print("\nИзвлечение минимума:")
min_val = heap.extract_min()
print(f"Извлечено: {min_val}")
print(f"Куча после извлечения: {heap} | Валидна: {heap.is_valid_heap()}")

print("\nПостроение кучи из массива [9, 4, 6, 2, 10]")
arr = [9, 4, 6, 2, 10]
heap.build_heap(arr)
print(f"Куча после построения: {heap} | Валидна: {heap.is_valid_heap()}")
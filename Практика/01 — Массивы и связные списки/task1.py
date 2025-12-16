class StaticArray:
    def __init__(self, capacity):
        """Инициализация статического массива - O(n), где n = capacity"""
        self.capacity = capacity  # O(1)
        self.size = 0  # O(1)
        self.data = [None] * capacity  # O(n), где n = capacity

    def is_full(self):
        """Проверка заполненности - O(1)"""
        return self.size >= self.capacity  # O(1)

    def pushBack(self, value):
        """Добавление в конец - O(1) (если есть место)"""
        if self.is_full():  # O(1)
            print("Массив заполнен, нельзя добавить элемент")  # O(1)
            return False  # O(1)

        self.data[self.size] = value  # O(1)
        self.size += 1  # O(1)
        return True  # O(1)

    def pushFront(self, value):
        """Добавление в начало - O(n) (сдвиг всех элементов)"""
        if self.is_full():  # O(1)
            print("Массив заполнен, нельзя добавить элемент")  # O(1)
            return False  # O(1)

        for i in range(self.size, 0, -1):  # O(n) итераций
            self.data[i] = self.data[i - 1]  # O(1) на итерацию

        self.data[0] = value  # O(1)
        self.size += 1  # O(1)
        return True  # O(1)

    def insert(self, index, value):
        """Вставка по индексу - O(n) (в худшем случае сдвиг всех элементов)"""
        if index < 0 or index > self.size:  # O(1)
            print(f"Индекс {index} вне диапазона [0, {self.size}]")  # O(1)
            return False  # O(1)

        if self.is_full():  # O(1)
            print("Массив заполнен, нельзя добавить элемент")  # O(1)
            return False  # O(1)

        for i in range(self.size, index, -1):  # O(n) итераций в худшем случае
            self.data[i] = self.data[i - 1]  # O(1) на итерацию

        self.data[index] = value  # O(1)
        self.size += 1  # O(1)
        return True  # O(1)

    def remove(self, index):
        """Удаление по индексу - O(n) (в худшем случае сдвиг всех элементов)"""
        if index < 0 or index >= self.size:  # O(1)
            print(f"Индекс {index} вне диапазона [0, {self.size - 1}]")  # O(1)
            return False  # O(1)

        for i in range(index, self.size - 1):  # O(n) итераций в худшем случае
            self.data[i] = self.data[i + 1]  # O(1) на итерацию

        self.data[self.size - 1] = None  # O(1)
        self.size -= 1  # O(1)
        return True  # O(1)

    def find(self, value):
        """Поиск по значению - O(n) (линейный поиск)"""
        for i in range(self.size):  # O(n) итераций в худшем случае
            if self.data[i] == value:  # O(1) на итерацию
                return i  # O(1)
        return -1  # O(1)

    def __str__(self):
        """Строковое представление - O(n)"""
        elements = []  # O(1)
        for i in range(self.size):  # O(n) итераций
            elements.append(str(self.data[i]))  # O(1) на итерацию
        return "[" + ", ".join(elements) + f"] (size={self.size}, capacity={self.capacity})"  # O(n)

    def get(self, index):
        """Получение элемента по индексу - O(1) (прямой доступ)"""
        if index < 0 or index >= self.size:  # O(1)
            raise IndexError(f"Индекс {index} вне диапазона")  # O(1)
        return self.data[index]  # O(1)


if __name__ == "__main__":
    print("=== Тестирование статического массива ===")
    print("Все операции выполняются с указанием временной сложности (Big O)\n")

    arr = StaticArray(5)
    print(f"Создан статический массив емкостью 5 - O(n)")

    print("\n1. Добавляем элементы в конец (O(1)):")
    arr.pushBack(10)
    arr.pushBack(20)
    arr.pushBack(30)
    print(f"   После pushBack(10, 20, 30): {arr}")

    print("\n2. Добавляем элемент в начало (O(n)):")
    arr.pushFront(5)
    print(f"   После pushFront(5): {arr}")

    print("\n3. Вставляем элемент по индексу (O(n)):")
    arr.insert(2, 15)
    print(f"   После insert(2, 15): {arr}")

    print("\n4. Ищем элементы (O(n)):")
    print(f"   find(15) = {arr.find(15)}")
    print(f"   find(99) = {arr.find(99)}")

    print("\n5. Получаем элементы по индексу (O(1)):")
    print(f"   get(0) = {arr.get(0)}")
    print(f"   get(3) = {arr.get(3)}")

    print("\n6. Удаляем элемент по индексу (O(n)):")
    arr.remove(1)
    print(f"   После remove(1): {arr}")

    print("\n7. Проверяем переполнение:")
    arr.pushBack(40)
    arr.pushBack(50)
    print(f"   После pushBack(40, 50): {arr}")

    print("\n8. Попытка добавить в заполненный массив:")
    arr.pushBack(60)
    print(f"   После попытки pushBack(60): {arr}")

    print("\n" + "=" * 60)
    print("Сводка по временной сложности операций:")
    print("• pushBack(value): O(1)")
    print("• pushFront(value): O(n)")
    print("• insert(index, value): O(n)")
    print("• remove(index): O(n)")
    print("• find(value): O(n)")
    print("• get(index): O(1)")
    print("• __init__(capacity): O(n)")
    print("=" * 60)
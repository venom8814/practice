import time


class StaticArray:
    """Версия StaticArray для использования внутри task2"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def is_full(self):
        return self.size >= self.capacity

    def pushBack(self, value):
        if self.is_full():
            return False

        self.data[self.size] = value
        self.size += 1
        return True


class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * initial_capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def pushBack(self, value):
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1
        return True

    def pushFront(self, value):
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]

        self.data[0] = value
        self.size += 1
        return True

    def insert(self, index, value):
        if index < 0 or index > self.size:
            print(f"Индекс {index} вне диапазона [0, {self.size}]")
            return False

        if self.size >= self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.size:
            print(f"Индекс {index} вне диапазона [0, {self.size - 1}]")
            return False

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1
        return True

    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def __str__(self):
        elements = []
        for i in range(self.size):
            elements.append(str(self.data[i]))
        return "[" + ", ".join(elements) + f"] (size={self.size}, capacity={self.capacity})"


def demo_dynamic_array():
    print("=== Демонстрация динамического массива ===")

    arr = DynamicArray(3)
    print(f"Создан динамический массив с начальной емкостью 3")

    print("\n1. Добавляем элементы до переполнения:")
    for i in range(1, 5):
        arr.pushBack(i * 10)
        print(f"   Добавлен {i * 10}: {arr}")

    # Показываем вставку в начало и середину
    print("\n2. Тестируем другие операции:")
    arr.pushFront(5)
    print(f"   После pushFront(5): {arr}")

    arr.insert(2, 25)
    print(f"   После insert(2, 25): {arr}")

    print(f"\n3. Поиск и удаление:")
    print(f"   find(25) = {arr.find(25)}")
    print(f"   find(99) = {arr.find(99)}")

    arr.remove(2)
    print(f"   После remove(2): {arr}")


def compare_performance():
    num_elements = 100000

    print("\n" + "=" * 60)
    print("=== Сравнение производительности статического и динамического массивов ===")

    print(f"\n1. Статический массив (емкость={num_elements}):")
    static_arr = StaticArray(num_elements)

    start_time = time.time()
    for i in range(num_elements):
        static_arr.pushBack(i)
    static_time = time.time() - start_time

    print(f"   Время: {static_time:.4f} сек")
    print(f"   Результат: {static_arr.size}/{static_arr.capacity} элементов")

    print(f"\n2. Статический массив (емкость={num_elements // 2}):")
    static_arr_small = StaticArray(num_elements // 2)

    start_time = time.time()
    added = 0
    for i in range(num_elements):
        if static_arr_small.pushBack(i):
            added += 1
    static_time_small = time.time() - start_time

    print(f"   Время: {static_time_small:.4f} сек")
    print(f"   Результат: {added}/{num_elements} элементов добавлено")

    print(f"\n3. Динамический массив (начальная емкость=10):")
    dynamic_arr = DynamicArray(10)

    start_time = time.time()
    for i in range(num_elements):
        dynamic_arr.pushBack(i)
    dynamic_time = time.time() - start_time

    print(f"   Время: {dynamic_time:.4f} сек")
    print(f"   Результат: {dynamic_arr.size}/{dynamic_arr.capacity} элементов")
    print(f"   Расширение: в {dynamic_arr.capacity / 10:.2f} раз")

    print(f"\n4. Динамический массив (начальная емкость=1000):")
    dynamic_arr2 = DynamicArray(1000)

    start_time = time.time()
    for i in range(num_elements):
        dynamic_arr2.pushBack(i)
    dynamic_time2 = time.time() - start_time

    print(f"   Время: {dynamic_time2:.4f} сек")
    print(f"   Результат: {dynamic_arr2.size}/{dynamic_arr2.capacity} элементов")
    print(f"   Расширение: в {dynamic_arr2.capacity / 1000:.2f} раз")

    print("\n" + "=" * 60)
    print("Итоги сравнения:")
    print(f"Динамический (емкость=10) медленнее статического в {dynamic_time / static_time:.2f} раз")
    print(f"Динамический (емкость=1000) медленнее статического в {dynamic_time2 / static_time:.2f} раз")


if __name__ == "__main__":
    demo_dynamic_array()
    compare_performance()
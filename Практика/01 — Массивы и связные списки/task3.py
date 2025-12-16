class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pushFront(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pushBack(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print(f"Индекс {index} вне диапазона [0, {self.length}]")
            return False

        if index == 0:
            return self.pushFront(value)

        if index == self.length:
            return self.pushBack(value)

        new_node = Node(value)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.length += 1
        return True

    def removeByValue(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return True

        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next

        if current.next is None:
            print(f"Значение {value} не найдено в списке")
            return False

        node_to_remove = current.next
        current.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = current

        self.length -= 1
        return True

    def removeFirst(self):
        if self.head is None:
            return False

        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.length -= 1
        return True

    def removeLast(self):
        if self.head is None:
            return False

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        self.length -= 1
        return True

    def find(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev = None
        current = self.head

        self.head, self.tail = self.tail, self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements) + f" (длина: {self.length})"


def demo_singly_linked_list():
    print("=== Демонстрация односвязного списка ===")

    sll = SinglyLinkedList()

    print("\n1. Тестируем добавление элементов:")
    sll.pushFront(30)
    sll.pushFront(20)
    sll.pushFront(10)
    print(f"   После pushFront(10, 20, 30): {sll}")

    sll.pushBack(40)
    sll.pushBack(50)
    print(f"   После pushBack(40, 50): {sll}")

    print("\n2. Тестируем вставку по индексу:")
    sll.insert(2, 25)
    print(f"   После insert(2, 25): {sll}")
    sll.insert(5, 45)
    print(f"   После insert(5, 45): {sll}")

    print("\n3. Тестируем поиск:")
    print(f"   find(25) = {sll.find(25)}")
    print(f"   find(99) = {sll.find(99)}")

    print("\n4. Тестируем удаление:")
    sll.removeByValue(25)
    print(f"   После removeByValue(25): {sll}")
    sll.removeByValue(10)
    print(f"   После removeByValue(10): {sll}")
    sll.removeByValue(99)

    print("\n5. Тестируем удаление первого и последнего:")
    sll.removeFirst()
    print(f"   После removeFirst(): {sll}")
    sll.removeLast()
    print(f"   После removeLast(): {sll}")

    print("\n6. Тестируем разворот списка:")
    # Восстанавливаем список для демонстрации
    for i in [1, 2, 3, 4, 5]:
        sll.pushBack(i)
    print(f"   Список до разворота: {sll}")
    sll.reverse()
    print(f"   Список после разворота: {sll}")

    print(f"\n7. Конвертация в обычный список: {sll.to_list()}")


def compare_with_array():
    print("\n" + "=" * 60)
    print("=== Сравнение с массивом ===")

    print("\nКлючевые различия:")
    print("1. Вставка в начало:")
    print("   - Список: O(1) - меняем указатель head")
    print("   - Массив: O(n) - сдвигаем все элементы")

    print("\n2. Вставка в конец:")
    print("   - Список (с tail): O(1) - меняем указатель tail")
    print("   - Массив: O(1) если есть место, иначе O(n) при расширении")

    print("\n3. Доступ по индексу:")
    print("   - Список: O(n) - нужно пройти от начала")
    print("   - Массив: O(1) - прямой доступ")

    print("\n4. Удаление из начала:")
    print("   - Список: O(1) - меняем указатель head")
    print("   - Массив: O(n) - сдвигаем все элементы")

    print("\n5. Память:")
    print("   - Список: больше памяти (данные + указатель)")
    print("   - Массив: компактнее (только данные)")


if __name__ == "__main__":
    demo_singly_linked_list()
    compare_with_array()
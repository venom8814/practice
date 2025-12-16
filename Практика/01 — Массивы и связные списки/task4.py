class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pushFront(self, value):
        new_node = DNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pushBack(self, value):
        new_node = DNode(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def insertAfterNode(self, node, value):
        if node is None:
            print("Ошибка: передан None узел")
            return False

        new_node = DNode(value)

        new_node.prev = node
        new_node.next = node.next

        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node

        if node == self.tail:
            self.tail = new_node

        self.length += 1
        return True

    def insertBeforeNode(self, node, value):
        if node is None:
            print("Ошибка: передан None узел")
            return False

        new_node = DNode(value)

        new_node.next = node
        new_node.prev = node.prev

        if node.prev is not None:
            node.prev.next = new_node
        node.prev = new_node

        if node == self.head:
            self.head = new_node

        self.length += 1
        return True

    def deleteNodeDirectly(self, node):
        if node is None:
            print("Ошибка: передан None узел")
            return False

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

        self.length -= 1
        return True

    def deleteByValue(self, value):
        node = self._find_node_by_value(value)
        if node is None:
            print(f"Узел со значением {value} не найден")
            return False

        return self.deleteNodeDirectly(node)

    def _find_node_by_value(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def get_node_at(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - index):
                current = current.prev

        return current

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        self.head, self.tail = self.tail, self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

    def to_list_forward(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def to_list_backward(self):
        result = []
        current = self.tail
        while current is not None:
            result.append(current.data)
            current = current.prev
        return result

    def __str__(self):
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return " <-> ".join(elements) + f" (длина: {self.length})"


class DoublyLinkedListIterator:
    def __init__(self, dll):
        self.current = dll.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


class DoublyLinkedListReverseIterator:
    def __init__(self, dll):
        self.current = dll.tail

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.prev
        return data


def demo_doubly_linked_list():
    print("=== Демонстрация двусвязного списка ===")

    dll = DoublyLinkedList()

    print("\n1. Тестируем добавление элементов:")
    dll.pushFront(30)
    dll.pushFront(20)
    dll.pushFront(10)
    print(f"   После pushFront(10, 20, 30): {dll}")

    dll.pushBack(40)
    dll.pushBack(50)
    print(f"   После pushBack(40, 50): {dll}")

    print("\n2. Тестируем вставку после узла:")
    node = dll.get_node_at(2)  # Узел со значением 30
    if node:
        dll.insertAfterNode(node, 35)
        print(f"   После insertAfterNode(узел_30, 35): {dll}")

    print("\n3. Тестируем вставку перед узлом:")
    node = dll.get_node_at(3)  # Узел со значением 35
    if node:
        dll.insertBeforeNode(node, 32)
        print(f"   После insertBeforeNode(узел_35, 32): {dll}")

    print("\n4. Тестируем удаление узла напрямую:")
    node = dll.get_node_at(3)  # Узел со значением 32
    if node:
        dll.deleteNodeDirectly(node)
        print(f"   После deleteNodeDirectly(узел_32): {dll}")

    print("\n5. Тестируем удаление по значению:")
    dll.deleteByValue(35)
    print(f"   После deleteByValue(35): {dll}")
    dll.deleteByValue(99)  # Несуществующее значение

    print("\n6. Тестируем итераторы:")
    print("   Прямой обход:", end=" ")
    for value in DoublyLinkedListIterator(dll):
        print(value, end=" ")
    print()

    print("   Обратный обход:", end=" ")
    for value in DoublyLinkedListReverseIterator(dll):
        print(value, end=" ")
    print()

    print("\n7. Тестируем разворот списка:")
    print(f"   До разворота: {dll}")
    dll.reverse()
    print(f"   После разворота: {dll}")

    print(f"\n8. Конвертация в списки:")
    print(f"   Вперед: {dll.to_list_forward()}")
    print(f"   Назад:  {dll.to_list_backward()}")


def compare_with_singly_linked():
    print("\n" + "=" * 60)
    print("=== Сравнение с односвязным списком ===")

    print("\nПреимущества двусвязного списка:")
    print("1. Удаление известного узла: O(1) (в односвязном O(n))")
    print("2. Вставка перед узлом: O(1) (в односвязном O(n))")
    print("3. Двунаправленный обход (вперед и назад)")
    print("4. Удаление последнего элемента: O(1) с tail")

    print("\nНедостатки двусвязного списка:")
    print("1. Больше памяти (данные + 2 указателя)")
    print("2. Сложнее реализация (нужно обновлять оба указателя)")
    print("3. Больше операций при вставке/удалении")

    print("\nКогда использовать двусвязный список:")
    print("- Нужен двунаправленный обход")
    print("- Нужна эффективная вставка перед узлом")
    print("- Реализация навигации (вперед/назад)")

    print("\nКогда использовать односвязный список:")
    print("- Важна экономия памяти")
    print("- Только однонаправленный обход")
    print("- Удаления преимущественно с начала")
    print("- Простота реализации важнее производительности")


if __name__ == "__main__":
    demo_doubly_linked_list()
    compare_with_singly_linked()
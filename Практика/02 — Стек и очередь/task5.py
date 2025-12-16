class StackArray:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Стек пуст")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Стек пуст")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            raise IndexError("Стек пуст")
        return self.top.data

    def is_empty(self):
        return self.top is None


def check_brackets(sequence):
    stack = StackArray()
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != brackets_map[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    sa = StackArray()
    sa.push(1)
    sa.push(2)
    print("Стек (массив):", sa.pop(), sa.pop())  # 2, 1

    sl = StackLinkedList()
    sl.push('a')
    sl.push('b')
    print("Стек (список):", sl.pop(), sl.pop())  # b, a

    test_cases = ["()", "([]{})", "(]", "([)]", "{[()]}", "((()))"]
    for expr in test_cases:
        result = check_brackets(expr)
        print(f"'{expr}' -> {'Верно' if result else 'Ошибка'}")
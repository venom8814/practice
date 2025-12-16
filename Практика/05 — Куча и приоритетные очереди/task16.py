import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, value, priority):
        heapq.heappush(self.heap, (priority, self.counter, value))
        self.counter += 1

    def pop(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        priority, _, value = heapq.heappop(self.heap)
        return value, priority

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str([(p, v) for p, _, v in self.heap])
pq = PriorityQueue()

print("\nДобавляем задачи с приоритетами:")
tasks = [
    ("Отправить отчёт", 3),
    ("Позвонить клиенту", 1),
    ("Написать письмо", 2),
    ("Собрание", 1),
    ("Обновить документацию", 4)
]

for task, prio in tasks:
    pq.push(task, prio)
    print(f"Добавлено: {task} (приоритет {prio})")

print(f"\nОчередь: {pq}")

print("\nИзвлекаем задачи по приоритету (от самой важной):")
while not pq.is_empty():
    task, prio = pq.pop()
    print(f"Выполняем: {task} (приоритет {prio})")


print("\n ПРИМЕНЕНИЕ: ПОИСК МИНИМАЛЬНЫХ ЭЛЕМЕНТОВ ")

numbers = [45, 12, 78, 3, 99, 21, 6, 55]
print(f"Исходный массив: {numbers}")

pq_nums = PriorityQueue()
for num in numbers:
    pq_nums.push(num, num)

print("Извлекаем 3 минимальных элемента:")
for i in range(3):
    if not pq_nums.is_empty():
        min_num, _ = pq_nums.pop()
        print(f"{i+1}-й минимальный: {min_num}")
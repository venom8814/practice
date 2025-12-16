class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Очередь переполнена")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Очередь пуста")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.size == 0:
            raise IndexError("Очередь пуста")
        return self.queue[self.front]


class QueueTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Очередь пуста")
        return self.stack_out.pop()

    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Очередь пуста")
        return self.stack_out[-1]


if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("Цикл. очередь:", cq.dequeue(), cq.dequeue(), cq.dequeue())  # 10, 20, 30

    qts = QueueTwoStacks()
    qts.enqueue(100)
    qts.enqueue(200)
    qts.enqueue(300)
    print("Очередь на стеках:", qts.dequeue(), qts.dequeue(), qts.dequeue())  # 100, 200, 300
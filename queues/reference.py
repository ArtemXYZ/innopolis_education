
queue = []
queue.append(1)  # Добавляем элемент 1 в конец очереди
queue.append(2)  # Добавляем элемент 2 в конец очереди
queue.append(3)  # Добавляем элемент 3 в конец очереди
print(queue.pop(0))  # Удаляем и возвращаем первый элемент: 1

print(queue)


from collections import deque

queue = deque()      # Создаем пустую очередь
queue.append(1)      # Добавляем элемент 1
queue.append(2)      # Добавляем элемент 2
queue.append(3)      # Добавляем элемент 3
print(queue.popleft())  # Удаляем и возвращаем первый элемент: 1


dq = deque()
dq.append(1)         # Добавляем элемент 1 в конец
dq.appendleft(2)     # Добавляем элемент 2 в начало
print(dq.pop())      # Удаляем и возвращаем последний элемент: 1
print(dq.popleft())  # Удаляем и возвращаем первый элемент: 2


import heapq

pq = []
heapq.heappush(pq, (1, 'low priority task'))    # Добавляем задачу с низким приоритетом
heapq.heappush(pq, (0, 'high priority task'))   # Добавляем задачу с высоким приоритетом
print(heapq.heappop(pq))  # Извлекаем задачу с наивысшим приоритетом: (0, 'high priority task')



import queue
import threading

def worker(q):
    while not q.empty():
        item = q.get()
        print(f'Processing {item}')
        q.task_done()

q = queue.Queue()
for i in range(5):
    q.put(i)

thread = threading.Thread(target=worker, args=(q,))
thread.start()
q.join()  # Ожидание завершения обработки всех задач


#
#         Характеристика        |    Простая очередь (list)    |      collections.deque       | Приоритетная очередь (heapq)
# ---------------------------------------------------------------------------------------------------------------------------
# | Временная сложность Enqueue  |             O(1)             |             O(1)             |           O(log n)           |
# | Временная сложность Dequeue  |             O(n)             |             O(1)             |           O(log n)           |
# | Порядок обработки элементов  |             FIFO             |        FIFO или LIFO         |        По приоритету         |
# |     Простота реализации      |           Простая            |          Умеренная           |           Средняя            |
# |      Потокобезопасность      |             Нет              |             Нет              |             Нет              |
# |       Многопоточность        |          Ограничена          |          Ограничена          |          Ограничена          |
# |     Использование памяти     |           Высокое            |            Низкое            |            Низкое            |
# |    Примеры использования     | Малые данные, простые задачи |Обработка данных в реальном времени, LIFO задачи|Планировщики задач,
#                                                                                                                         поиск путей|


class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.queue.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди."""
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.queue)


# Пример использования
q = SimpleQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.size())  # 2


from collections import deque


class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.queue.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди."""
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.queue)


# Пример использования
dq = DequeQueue()
dq.enqueue(1)
dq.enqueue(2)
dq.enqueue(3)
print(dq.dequeue())  # 1
print(dq.size())  # 2


import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        """Добавляет элемент в очередь с приоритетом."""
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        """Удаляет и возвращает элемент с наивысшим приоритетом."""
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.queue)


# Пример использования
pq = PriorityQueue()
pq.enqueue(2, 'low')
pq.enqueue(1, 'high')
print(pq.dequeue())  # 'high'
print(pq.size())  # 1


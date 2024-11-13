# Первая реализация использует список фиксированной длины, что имеет как плючы так и минусы.
# Плюсы : Простота, как в в реализации так и в работе с памятью, память выделяется один раз и не изменяется в процессе.
# Минусы: Однако фиксированный размер также имеет и проблемы, так как он должен быть известен заранее.
# Быстродействие: enqueue и dequeue будут выполняться за O(1)
# Вторая реализация использует динамический список.
# Плюсы : Благодаря возможности возможности менять размер динамически теперь нет необходимости знать размер заранее.
# Минусы : По сравнению с первой реализацией код сложнее, при больших размерах возможны проблемы с потреблением памяти.
# Быстродействие : Вставка при худшем случае (если буффер полон) будет выполняться за O(n). Удаление имеет то же время.

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    class DynamicCircularBuffer:
        def __init__(self, initial_size=10):
            self.buffer = [None] * initial_size
            self.head = 0
            self.tail = 0
            self.count = 0
            self.size = initial_size

        def is_full(self):
            return self.count == self.size

        def is_empty(self):
            return self.count == 0

        def _resize(self):
            new_size = self.size * 2
            new_buffer = [None] * new_size
            for i in range(self.count):
                new_buffer[i] = self.buffer[(self.head + i) % self.size]
            self.buffer = new_buffer
            self.head = 0
            self.tail = self.count
            self.size = new_size

        def enqueue(self, item):
            if self.is_full():
                self._resize()
            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.size
            self.count += 1

        def dequeue(self):
            if self.is_empty():
                raise IndexError("Buffer is emty")
            item = self.buffer[self.head]
            self.buffer[self.head] = None
            self.head = (self.head + 1) % self.size
            self.count -= 1
            return item

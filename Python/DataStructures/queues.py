from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
    
q = Queue()
q.enqueue(2)
q.enqueue(5)
q.enqueue(7)

q.dequeue()

for element in q:
    print(element)

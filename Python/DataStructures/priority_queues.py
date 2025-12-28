from queue import PriorityQueue

# min PQ by default
pq = PriorityQueue()
pq.put(2)
pq.put(1)
pq.put(4)

while not pq.empty():
    print(pq.get())

# max PQ trick
pq = PriorityQueue()
pq.put(-2)
pq.put(-1)
pq.put(-4)

while not pq.empty():
    print(-1 * pq.get())
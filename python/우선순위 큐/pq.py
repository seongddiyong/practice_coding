from queue import PriorityQueue
import heapq

q = PriorityQueue()
q.put(3)    # [3]
q.put(4)    # [4,3]
q.put(1)    # [1,4,3]
print(q.get())  # 1 [3,4]
print(q.get())  # 3 [4]
print(q.get())  # 4 []

h = heapq
hq = []

h.heappush(hq, 4)   # [4]
h.heappush(hq, 1)   # [1,4]
h.heappush(hq, 3)   # [1,4,3]
h.heappush(hq, 7)   # [1,4,3,7]
h.heappush(hq, 5)   # [1,4,3,7,5]

print(h.heappop(hq))    # 1 [3,4,5,7]
print(h.heappop(hq))    # 3 [4,7,5]
print(h.heappop(hq))    # 4 [5,7]
print(h.heappop(hq))    # 5 [7]
print(h.heappop(hq))    # 7 []

x = [4,6,1,3,2,7,6]
h.heapify(x)
print(x)
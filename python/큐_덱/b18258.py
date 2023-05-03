from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
queue = deque([])
for _ in range(n):
    order = input().rstrip()
    if " " in order:
        order2 = order.split(" ")
        queue.append(int(order2[1]))
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "pop":
        if queue:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

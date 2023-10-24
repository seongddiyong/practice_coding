from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    t = input().rstrip()
    if len(t) > 5:
        q.append(int(t[5:]))
    elif t == "pop":
        if q: print(q.popleft())
        else: print(-1)
    elif t == "size":
        print(len(q))
    elif t == "empty":
        if q: print(0)
        else: print(1)
    elif t == "front":
        if q: print(q[0])
        else: print(-1)
    else:
        if q: print(q[-1])
        else: print(-1)
import heapq
from sys import stdin
input = stdin.readline
h = heapq

n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if hq:
            print(h.heappop(hq))
        else: print(0)
    else:
        h.heappush(hq, x)
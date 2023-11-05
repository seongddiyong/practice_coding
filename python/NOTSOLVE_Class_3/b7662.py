from sys import stdin
import heapq
input = stdin.readline
h = heapq
q = []
for t in range(int(input())):
    for k in range(int(input())):
        c, n = input().rstrip()
        n = int(n)
        if c == "I":
            h.heappush(q,n)
        else:
            if n == -1:
                
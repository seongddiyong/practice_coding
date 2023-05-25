from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
w = deque(sorted([int(input()) for _ in range(n)]))
result = []
i = 0
while w:
    result.append(w[0] * (n-i))
    w.popleft()
    i += 1
print(max(result))
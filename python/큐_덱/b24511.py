from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q = deque([])
for i in range(n):
    if a[i] == 0:
        q.appendleft(b[i])
m = int(input())
c = list(map(int, input().split()))
for i in c:
    q.append(i)
    print(q.popleft(), end=" ")
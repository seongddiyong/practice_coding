from sys import stdin
input = stdin.readline
from collections import deque
n,k = map(int, input().split())
p = deque([i for i in range(1,n+1)])
result = []
while p:
    for i in range(k-1):
        p.append(p.popleft())
    result.append(p.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")
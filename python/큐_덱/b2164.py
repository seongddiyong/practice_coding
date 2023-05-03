from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
temp = deque([i for i in range(1,n+1)])
while len(temp) > 1:
    temp.popleft()
    a = temp.popleft()
    temp.append(a)
print(temp[0])
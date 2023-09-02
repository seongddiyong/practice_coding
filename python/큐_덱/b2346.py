from sys import stdin
from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))
while queue:
    index, num = queue.popleft()
    print(index+1, end=' ')
    if num > 0:
        queue.rotate(-(num - 1))
    else:
        queue.rotate(-num)

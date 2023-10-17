from sys import stdin
from collections import deque
input = stdin.readline

n,k = map(int, input().split())
q = deque([i+1 for i in range(n)])
cnt = 1
answer = []
while q:
    for _ in range(k-1):
        q.rotate(-1)
    answer.append(q.popleft())
print(str(answer).replace('[', '<').replace(']', '>'))
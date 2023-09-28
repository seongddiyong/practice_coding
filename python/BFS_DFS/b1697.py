from sys import stdin
from collections import deque
input = stdin.readline

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return array[v]
        for nv in (v-1,v+1,v*2):
            if 0 <= nv < m and not array[nv]:
                array[nv] = array[v] + 1
                queue.append(nv)

n,k = map(int, input().split())
m = 100001
array = [0] * m
print(bfs(n))
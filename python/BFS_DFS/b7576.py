import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip().split())))
ans = 0
queue = deque()

def bfs():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()

for i in graph:
    if 0 in i:
        print(-1)
        exit(0)
    ans = max(ans, max(i))
print(ans - 1)
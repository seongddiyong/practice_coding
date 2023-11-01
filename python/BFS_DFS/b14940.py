from sys import stdin
from collections import deque
input = stdin.readline
n,m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[-1]*m for _ in range(n)]

def bfs(st_x, st_y):
    q = deque()
    q.append([st_x,st_y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1 and ground[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([nx,ny])

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            visited[i][j] = 0
            bfs(j,i)
        elif ground[i][j] == 0:
            visited[i][j] = 0

for i in visited:
    for j in i:
        print(j, end=' ')
    print()
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int,input().rstrip())) for _ in range(n)]

def bfs(x,y):
    cnt = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 넘기기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이면 넘기기
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니라면?
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))

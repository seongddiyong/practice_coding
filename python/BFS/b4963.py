from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx,ny])

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def bfs(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx
            ny = y + dy
            # 범위 벗어나면 넘기기
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            # 물이면 넘기기
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[0]*w for _ in range(h)]
    
    cnt = 0
    bfs(0,0)
    print(cnt)
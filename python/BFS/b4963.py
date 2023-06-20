from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def dfs(x,y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)
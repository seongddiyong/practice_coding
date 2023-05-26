import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                dfs(nx,ny)
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            cnt += 1
            dfs(i,j)

print(cnt,end=' ')
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            cnt += 1
            dfs(i,j)

print(cnt)
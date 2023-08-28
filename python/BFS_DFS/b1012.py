import sys
sys.setrecursionlimit(10000)
t = int(input())

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return 0
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return 1
    return 0

for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for q in range(n)]
    cnt = 0
    # x,y 좌표를 받고, 그 곳에 배추를 심는다.
    for i in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == 1:
                cnt += 1
    print(cnt)
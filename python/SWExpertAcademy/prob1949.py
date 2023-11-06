from sys import stdin
from collections import deque
input = stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,path,pos):
    global answer
    if answer < path:
        answer = path
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 이동 가능
            if graph[x][y] > graph[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,path+1,pos)
                visited[nx][ny] = False
            # 이동이 불가능하고 아직 공사를 안 했으면
            elif graph[x][y] <= graph[nx][ny] and not pos:
                for j in range(1,K+1):
                    graph[nx][ny] -= j
                    pos = True
                    if graph[x][y] > graph[nx][ny]:
                        visited[nx][ny] = True
                        dfs(nx,ny,path+1,pos)
                        visited[nx][ny] = False
                    pos = False
                    graph[nx][ny] += j

for t in range(int(input())):
    N, K = map(int, input().split())
    graph = []
    maximum = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        graph.append(temp)
        if maximum < max(temp):
            maximum = max(temp)
    answer = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == maximum:
                visited = [[False]*N for _ in range(N)]
                visited[i][j] = 1
                dfs(i,j,1,False)
    print('#{} {}'.format(t+1, answer))
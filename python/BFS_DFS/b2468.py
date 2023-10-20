from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
g = []
maxn = 1
minn = 101
for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)
    if max(temp) > maxn:
        maxn = max(temp)
dy = [0,0,-1,1]
dx = [1,-1,0,0]

def bfs(h,a,b,v):
    q = deque()
    q.append([a,b])
    v[a][b] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] > h and v[nx][ny] == False:
                    v[nx][ny] = True
                    q.append([nx,ny])
        

answer = 0
for h in range(maxn):
    v = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and v[i][j] == False:
                bfs(h,i,j,v)
                cnt += 1
    if answer < cnt:
        answer = cnt
print(answer)
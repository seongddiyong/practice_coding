from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

# def dfs(x,y):
#     global cnt
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return
#     # 집일 때
#     if graph[x][y] == 1:
#         cnt += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx,ny)

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx,ny])
                cnt += 1
    return cnt

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
result = []
# cnt = 0

# 상 / 하 / 좌 / 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i,j)
#             result.append(cnt)
#             cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = bfs(i,j)
            result.append(cnt)

ans = sorted(result)
print(len(result))
for i in ans:
    print(i)
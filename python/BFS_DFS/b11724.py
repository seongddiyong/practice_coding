import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

visited = [False] * (n+1)
cnt = 0

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

for i in range(1,n+1):
    if visited[i] == False:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i)
            cnt += 1
print(cnt)
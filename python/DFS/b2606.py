computer = int(input())
network = int(input())

graph = [[]*(computer+1) for _ in range(computer+1)]
visited = [0] * (computer+1)

for _ in range(network):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited)-1)
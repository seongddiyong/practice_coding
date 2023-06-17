from collections import deque

computer = int(input())
network = int(input())

graph = [[] for _ in range(computer+1)]
visited = [0] * (computer+1)

for _ in range(network):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        popv = queue.popleft()
        visited[popv] = 1
        for i in graph[popv]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

bfs(1)
print(sum(visited)-1)
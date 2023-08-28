n = int(input())

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    global cnt
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

graph = []
cnt = 0         # 집 개수를 세는 변수
result = []     # 각각의 집 개수를 넣을 리스트

for i in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result.append(cnt)
            cnt = 0

result = sorted(result)
print(len(result))
for i in result:
    print(i)

T = int(input())
f = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

def nine(x,y,checkNum,graph):
    check = [1,0,0,0,0,0,0,0,0,0]
    check[checkNum] = 1
    for i,j in f:
        cx = x + i
        cy = y + j
        if check[graph[cy][cx]]:
            return False
        else:
            check[graph[cy][cx]] = 1
    return True

def hv(graph):
    for i in range(9):
        check1 = [1,0,0,0,0,0,0,0,0,0]
        check2 = [1,0,0,0,0,0,0,0,0,0]
        for j in range(9):
            if check1[graph[i][j]] or check2[graph[j][i]]:
                return False
            else:
                check1[graph[i][j]] = check2[graph[j][i]] = 1
    return True

for t in range(1,T+1):
    answer = 1
    graph = [list(map(int, input().split())) for _ in range(9)]
    if not hv(graph):
        answer = 0
    else: 
        for x,y in [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]:
            if not nine(x,y,graph[y][x],graph):
                answer = 0
                break
    print(f"#{t} {answer}")
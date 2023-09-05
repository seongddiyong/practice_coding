from collections import deque

def bfs(x,y,n,m,maps):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and maps[ny][nx] == 1:
                queue.append([nx,ny])
                maps[ny][nx] += maps[y][x]
    return maps[m-1][n-1]

def solution(maps):
    n = len(maps[0])    # x
    m = len(maps)       # y
    answer = bfs(0,0,n,m,maps)
    if answer == 1:
        return -1
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
import sys
input = sys.stdin.readline

move = [(0,1), (0,-1), (1,0), (-1,0)]

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

maxValue = 0

def dfs(x, y, dsum, cnt):
    global maxValue
    # 모양이 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + board[nx][ny], cnt+1)

def exce(x, y):
    global maxValue
    for i in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[x][y]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (i+k)%4
            nx = x+move[t][0]
            ny = y+move[t][1]

            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += board[nx][ny]
        # 최대값 계산
        maxValue = max(maxValue, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exce(i,j)

print(maxValue)
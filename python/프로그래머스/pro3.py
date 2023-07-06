def solution(board):
    n = len(board)
    temp = [[0]*n for _ in range(n)]
    dx = [0,0,-1,1,-1,1,-1,1]
    dy = [1,-1,0,0,1,1,-1,-1]
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                temp[i][j] = 1
                for s in range(8):
                    nx = i+dx[s]
                    ny = j+dy[s]
                    if 0 <= nx < n and 0 <= ny < n:
                        temp[nx][ny] = 1
    for i in temp:
        answer += i.count(0)
    return answer

def solution2(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))
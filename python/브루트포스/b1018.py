import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = []     # 전체 보드를 나타낼 리스트
result = []     # 결과값을 나타낼 리스트

for _ in range(n):
    board.append(input())      # 전체 보드를 append를 통해 입력 받음

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
        for a in range(i,i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)
 
print(min(result))


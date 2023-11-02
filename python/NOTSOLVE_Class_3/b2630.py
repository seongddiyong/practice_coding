from sys import stdin
input = stdin.readline
n = int(input())
p = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
w = b = 0

def solution(x, y, N):
    global w,b
    color = p[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != p[i][j]:
                solution(x,y,N//2)
                solution(x,y+N//2,N//2)
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        w += 1
    else:
        b += 1

solution(0,0,n)
print(w)
print(b)
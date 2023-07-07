def right(x,y,num,n,answer):
    if num == n*n:
        return
    if x+1 >= n or answer[y][x+1] != 0:
        down(x,y,num,n,answer)
    else:
        answer[y][x+1] = num+1
        num += 1
        right(x+1,y,num,n,answer)
        
def down(x,y,num,n,answer):
    if num == n*n:
        return
    if y+1 >= n or answer[y+1][x] != 0:
        left(x,y,num,n,answer)
    else:
        answer[y+1][x] = num+1
        num += 1
        down(x,y+1,num,n,answer)
        
def left(x,y,num,n,answer):
    if num == n*n:
        return
    if x-1 < 0 or answer[y][x-1] != 0:
        up(x,y,num,n,answer)
    else:
        answer[y][x-1] = num+1
        num += 1
        left(x-1,y,num,n,answer)

def up(x,y,num,n,answer):
    if num == n*n:
        return
    if y-1 < 0 or answer[y-1][x] != 0:
        right(x,y,num,n,answer)
    else:
        answer[y-1][x] = num+1
        num += 1
        up(x,y-1,num,n,answer)
        
def solution(n):
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    right(0,0,1,n,answer)
    return answer

solution(4)
from sys import stdin
input = stdin.readline
x,y = map(int, input().split())
start = 0
end = x
z = (y*100)//x
answer = x
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2
        if (100*(y+mid)//(x+mid)) > z:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(answer)
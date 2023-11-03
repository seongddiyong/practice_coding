from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
t = list(map(int, input().split()))
start, end = 1, max(t)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in t:
        if i > mid:
            cnt += i - mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
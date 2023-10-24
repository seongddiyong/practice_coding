import sys
input = sys.stdin.readline
k,n = map(int, input().split())
temp = []
for _ in range(k):
    temp.append(int(input()))
start, end = 1, max(temp)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in temp:
        cnt += i//mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid-1
print(end)
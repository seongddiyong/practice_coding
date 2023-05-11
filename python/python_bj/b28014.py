import sys
input = sys.stdin.readline
n = int(input())

temp = list(map(int, input().split()))
cnt = 1
for i in range(1,n):
    if temp[i-1] <= temp[i]:
        cnt += 1
print(cnt)
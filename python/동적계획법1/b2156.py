import sys
input = sys.stdin.readline
n = int(input())
temp = [0]*(n+1)
for i in range(1,n+1):
    temp[i] = int(input())
d = [0]*(n+1)
if n == 1:
    print(temp[1])
elif n == 2:
    d[1] = temp[1]
    d[2] = temp[2] + d[1]
    print(d[n])
else:
    d[1] = temp[1]
    d[2] = temp[2] + d[1]
    d[3] = max(temp[3]+d[1],temp[3]+temp[2],d[2])
    for i in range(4,n+1):
        d[i] = max(temp[i]+d[i-2],temp[i]+temp[i-1]+d[i-3],d[i-1])
    print(max(d))
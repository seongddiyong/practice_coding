import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = [0,1,2,4] + [0] * (n-3)
    if n <= 3:
        print(d[n])
    else:
        for i in range(4,n+1):
            d[i] = d[i-3] + d[i-2] + d[i-1]
        print(d[n])
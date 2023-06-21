import sys
input = sys.stdin.readline
n = int(input())
d = [0,1,2,3] + [0]*(n-3)
if n <= 3:
    print(n%10007)
else:
    for i in range(4,n+1):
        d[i] = d[i-2] + d[i-1]
    print(d[n]%10007)
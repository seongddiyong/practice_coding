import sys
input = sys.stdin.readline
n,r,c = map(int, input().split())
start = [0,0]
snum = 0
smin = 0
while n != 1:
    smax = start[1] + 2**(n-1)
    t = 2**(n-1) - 1
    if start[0]<=r<=start[0]+t and start[1]<=c<=start[1]+t:
        n -= 1
        temp = 0
    elif start[0]<=r<=start[0]+t and smax <= c <= smax+t:
        n -= 1
        start[1] = smax
        temp = 1
    elif smax<=r<=smax+t and start[1]<=c<=start[1]+t:
        n -= 1
        start[0] = smax
        temp = 2
    else:
        n -= 1
        start = [smax,smax]
        temp = 3
    snum += temp * (4**n)
print(snum + (r - start[0])*2 + (c-start[1]))
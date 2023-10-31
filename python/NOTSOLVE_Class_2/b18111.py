import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
g = []
for _ in range(n):
    temp = list(map(int,input().split()))
    g = g + temp
cnt = 0
while True:
    g.sort()
    if len(set(g)) == 1:
        print(cnt, g[0])
        break
    maximum = max(g)
    i = 0
    if b > 0:
        while b:
            if g[i] < g[i+1]:
                b -= 1
                g[i] += 1
            else:
                i += 1
    elif b == 0:
        idx = g.index(maximum)
        for i in range(idx,len(g)):
            g[i] -= 1
            b += 1
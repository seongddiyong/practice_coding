from sys import stdin
input = stdin.readline
dx,dy = [0,0,-1,1],[1,-1,0,0]

n,m = map(int, input().split())
g = []
BR = [False]*2
for i in range(n):
    temp = input().rstrip()
    g.append(temp)
    if 'B' in temp and not BR[0]:
        B = [i,temp.index('B')]
        BR[0] = True
    if 'R' in temp and not BR[1]:
        R = [i,temp.index('R')]
        BR[1] = True

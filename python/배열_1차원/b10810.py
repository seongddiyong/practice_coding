from sys import stdin

n,m = map(int, stdin.readline().rstrip().split())
list = [0 for _ in range(n)]

for _ in range(m):
    a=0
    i,j,k = map(int, stdin.readline().rstrip().split())
    for a in range(i-1,j):
        list[a] = k
for _ in range(n):
    print(list[_], end=" ")
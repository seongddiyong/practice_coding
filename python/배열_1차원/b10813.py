from sys import stdin

n,m = map(int, stdin.readline().rstrip().split())
list = [i+1 for i in range(n)]
for _ in range(m):
    temp = 0
    i,j = map(int, stdin.readline().rstrip().split())
    i -= 1
    j -= 1
    list[i], list[j] = list[j], list[i]
for _ in range(n):
    print(list[_], end=" ")

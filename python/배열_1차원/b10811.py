from sys import stdin
n,m = map(int, stdin.readline().rstrip().split())
list = [i+1 for i in range(n)]
for x in range(m):
    i,j = map(int, stdin.readline().rstrip().split())
    i -= 1
    temp = list[i:j]
    temp.reverse()
    list[i:j] = temp
for _ in range(n):
    print(list[_], end=" ")
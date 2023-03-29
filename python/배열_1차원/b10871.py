from sys import stdin
n,x = map(int, stdin.readline().rstrip().split())
a = list(map(int, stdin.readline().rstrip().split()))
for i in a:
    if i < x:
        print(i, end=" ")
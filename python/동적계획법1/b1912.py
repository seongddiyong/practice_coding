from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [a[0]] + [-1000]*n
for i in range(1,n):
    d[i] = max(d[i-1] + a[i], a[i])
print(max(d))
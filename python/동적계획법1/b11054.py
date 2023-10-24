from sys import stdin
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = a[::-1]
d1 = [1] * n
d2 = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d1[i] = max(d1[i],d1[j]+1)
        if b[i] > b[j]:
            d2[i] = max(d2[i],d2[j]+1)
d2.reverse()
temp = [0]*n
for i in range(n):
    temp[i] = d1[i]+d2[i]
print(max(temp)-1)
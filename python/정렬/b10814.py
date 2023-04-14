from sys import stdin
input = stdin.readline

n = int(input())
temp = []
for _ in range(n):
    temp.append((input().split()))
result = sorted(temp, key = lambda x:x[0])
for i,j in result:
    print(i,j)
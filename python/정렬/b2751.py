from sys import stdin
input = stdin.readline

n = int(input())
temp = [int(input()) for _ in range(n)]
for i in sorted(temp):
    print(i)
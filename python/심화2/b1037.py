from sys import stdin
input = stdin.readline
n = int(input())
real = sorted(list(map(int, input().split())))
print(real[0]*real[-1])

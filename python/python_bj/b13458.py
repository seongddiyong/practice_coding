import sys
input = sys.stdin.readline
import math

n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())

cnt = 0
for i in a:
    i -= b
    cnt += 1
    if i > 0:
        cnt += math.ceil(i/c)
print(cnt)
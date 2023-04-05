import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
bee = 1
while n > bee:
    bee += 6*cnt
    cnt += 1

print(cnt)
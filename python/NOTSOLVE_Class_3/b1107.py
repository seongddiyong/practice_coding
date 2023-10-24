import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
er = list(input().split())
ans = abs(100 - n)
for i in range(1000001):
    for j in str(i):
        if j in er:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i-n))
print(ans)
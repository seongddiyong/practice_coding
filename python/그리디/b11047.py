from sys import stdin
input = stdin.readline
n,k = map(int,input().split())
coin = sorted([int(input()) for _ in range(n)],reverse=True)
result = 0
for i in coin:
    if k < i:
        pass
    result += k//i
    k %= i
    if k == 0: break
print(result)
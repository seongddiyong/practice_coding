from sys import stdin
input = stdin.readline

k = int(input())
ans = []
for _ in range(k):
    n = int(input())
    if n == 0:
        ans.pop()
    else:
        ans.append(n)
print(sum(ans))
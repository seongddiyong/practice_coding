import sys
n,k = map(int, sys.stdin.readline().split())
result = []
a = 1
for _ in range(n):
    if n%a == 0:
        result.append(a)
    a += 1
if len(result) < k:
    print("0")
else:
    print(result[k-1])
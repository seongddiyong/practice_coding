import math
f = math.factorial
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    if k > n:
        n,k = k,n
    print(f(n) // (f(k) * f(n-k)))
import sys
input = sys.stdin.readline

def r(a):
    return int(a) + (1 if a - int(a) >= 0.5 else 0)

n = int(input())
if n == 0:
    print(0)
else:
    cut = r(n*0.15)
    score = []
    for _ in range(n):
        score.append(int(input()))
    score.sort()
    ans = 0
    for i in range(cut,n-cut):
        ans += score[i]
    print(r(ans/(n-(cut*2))))
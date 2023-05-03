import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    imp = deque(list(map(int, input().split())))
    ans = 0
    target = imp[m]
    while len(imp) != 0:
        while imp[0] != max(imp):
            imp.append(imp.popleft())
            m -= 1
            if m < 0:
                m = int(len(imp)-1)
        poppop = imp.popleft()
        ans += 1
        if target == poppop and m == 0:
            break
        m -= 1
    print(ans)
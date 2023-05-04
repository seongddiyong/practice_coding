import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    num = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        num = deque()
    cnt = 0
    flag = 0
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if num:
                if cnt % 2 == 0:
                    num.popleft()
                else:
                    num.pop()
            else:
                flag = 1
                print("error")
                break
    if flag == 0:
        if cnt % 2 == 0:
            print("[" + ",".join(num) + "]")
        else:
            num.reverse()
            print("[" + ",".join(num) + "]")
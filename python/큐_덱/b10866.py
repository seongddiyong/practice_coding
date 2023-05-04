import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
result = deque([])
for _ in range(n):
    order = input().rstrip()
    p = order[1]
    if p == 'u':
        order = order.split(' ')
        if order[0] == 'push_front':
            result.appendleft(int(order[1]))
        else:
            result.append(int(order[1]))
    elif p == 'o':
        if result:
            if order == 'pop_front':
                print(result.popleft())
            else:
                print(result.pop())
        else:
            print(-1)
    elif p == 'i':
        print(len(result))
    elif p == 'm':
        if result:
            print(0)
        else: print(1)
    elif p == 'r':
        if result:
            print(result[0])
        else:
            print(-1)
    elif p == 'a':
        if result:
            print(result[-1])
        else:
            print(-1)
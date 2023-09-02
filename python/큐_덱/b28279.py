from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
queue = deque([])

for i in range(n):
    a = input()
    if ' ' in a:
        a,b = map(int,a.split())
    else:
        a = int(a)
    match a:
        case 1:
            queue.appendleft(b)
        case 2:
            queue.append(b)
        case 3:
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        case 4:
            if queue:
                print(queue.pop())
            else:
                print(-1)
        case 5:
            print(len(queue))
        case 6:
            if queue:
                print(0)
            else:
                print(1)
        case 7:
            if queue:
                print(queue[0])
            else:
                print(-1)
        case 8:
            if queue:
                print(queue[-1])
            else:
                print(-1)
    
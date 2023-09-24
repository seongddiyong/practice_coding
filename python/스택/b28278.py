from sys import stdin
input = stdin.readline
n = int(input())
stack = []
for _ in range(n):
    a = input().rstrip()
    if len(a) > 1:
        a,b = map(int,a.split(" "))
    a = int(a)
    if a == 1:
        stack.append(b)
    elif a == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(stack))
    elif a == 4:
        if stack: print(0)
        else: print(1)
    else:
        if stack: print(stack[-1])
        else: print(-1)
    
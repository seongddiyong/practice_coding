import sys
input = sys.stdin.readline

n = int(input())
answer = []
stack = []
no = 0
cur = 1

for i in range(n):
    a = int(input())
    while cur <= a:
        stack.append(cur)
        answer.append('+')
        cur += 1
    if stack[-1] == a:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        no = 1
        break

if no == 0:
    for i in answer:
        print(i)
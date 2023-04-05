#세탁소 사장 동혁

from sys import stdin

input = stdin.readline

t = int(input())
change = [25, 10, 5, 1]
for _ in range(t):
    answer = []
    c = int(input())
    for i in change:
        answer.append(c//i)
        c %= i
    for j in range(4):
        print(answer[j], end=" ")
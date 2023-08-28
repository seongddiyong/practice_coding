import sys
input = sys.stdin.readline

n = int(input())
a = n
cnt = 0
while True:
    cnt += 1
    A = n // 10
    B = n % 10
    C = A + B
    n = B*10 + C%10
    if int(a) == int(n):
        print(cnt)
        break
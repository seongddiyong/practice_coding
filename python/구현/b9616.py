from sys import stdin
input = stdin.readline

while True:
    m,n = map(int, input().split())
    a = max(m,n)
    b = min(m,n)
    answer = 0
    if m == 0 and n == 0:
        break
    if m == 1 or n == 1:
        print(a)
    elif m == n and m % 2 == 1:
        answer += 3
    for i in range(1,b,2):
        if i % 2 == 1:
            answer += i*(a-i+1)**2 - i*(a-i+1)*(a-b)
    print(answer)
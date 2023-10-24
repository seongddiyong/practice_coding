from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    st = input().rstrip()
    cnt = 0
    answer = 0
    for i in st:
        if i == "O":
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)
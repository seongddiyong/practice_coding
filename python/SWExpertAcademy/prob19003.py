TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    answer = cnt = 0
    palindrome = False
    isNot = []
    for _ in range(N):
        a = input().rstrip()
        if a != a[::-1]:
            isNot.append(a)
        else:
            palindrome = True
    for _ in range(len(isNot)):
        temp = isNot.pop()
        if temp[::-1] in isNot:
            cnt += 2
    answer = cnt*M
    if palindrome:
        answer += M
    print(f'#{tc} {answer}')
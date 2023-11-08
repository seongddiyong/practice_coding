from itertools import permutations
TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    answer = 0
    palindrome = []
    isNot = []
    for _ in range(N):
        a = input().rstrip()
        if a != a[::-1]:
            isNot.append(a)
        else:
            palindrome.append(a)
    for _ in range(len(isNot)):
        temp = isNot.pop(0)
        if temp[::-1] in isNot:
            isNot.append(temp)
    answer = len(isNot)*M
    if palindrome:
        answer += M
    print(f'#{tc} {answer}')
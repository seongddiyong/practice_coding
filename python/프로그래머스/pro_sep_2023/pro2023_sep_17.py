import math

def isPrime(s):
    s = int(s)
    if s <= 1:
        return False
    if s <= 3:
        return True
    if s % 2 == 0 or s % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(s)) + 1, 6):
        if s % i == 0 or s % (i + 2) == 0:
            return False
    return True

def solution(n, k):
    num = []
    answer = 0
    if k != 10:
        while True:
            num.append(n%k)
            n //= k
            if n == 0:
                num = num[::-1]
                break
    else:
        for i in str(n): num.append(int(i))
    temp = ""
    for i in num:
        if (i == 0 and len(temp) > 0):
            if isPrime(temp):
                answer += 1
                temp = ""
            else:
                temp = ""
        elif i != 0:
            temp += str(i)
    if len(temp) > 0:
        if isPrime(temp):
                answer += 1
                temp = ""
    return answer

print(solution(110011,10))
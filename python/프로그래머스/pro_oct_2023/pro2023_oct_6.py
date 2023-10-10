def solution(n):
    ans = 0
    while True:
        if n%2 == 1:
            n -= 1
            ans += 1
        else:
            n //= 2
        if n == 0:
            break
    return ans
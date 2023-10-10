def solution(n,a,b):
    if a > b:
        a,b = b,a
    ans = 0
    while True:
        if abs(b-a) == 1 and a%2 == 1:
            ans += 1
            return ans
        a = a//2 + a%2
        b = b//2 + b%2
        ans += 1
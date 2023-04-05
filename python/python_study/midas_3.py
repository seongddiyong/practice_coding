import time

def solution(n, v, A, B, C):
    answer = -1
    AB = sorted([a * b for a in A for b in B if a * b <= v])
    C = sorted([c for c in C if c <= v])
    for ab in AB:
        for c in C:
            if ab * c <= v:
                answer = max(answer, ab * c)
            else:
                break
    return answer

n = 3
v = 101
A = [1, 2, 3]
B = [4, 5, 6]
C = [10, 11, 12]

start_ms = int(round(time.time() * 1000))
solution(n, v, A, B, C)
end_ms = int(round(time.time() * 1000))
print("1 ::: ", end_ms - start_ms)
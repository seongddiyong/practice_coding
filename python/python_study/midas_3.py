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
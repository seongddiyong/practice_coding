def solution(targets):
    answer = s = e = 0
    targets.sort(key = lambda x: x[1])
    for a,b in targets:
        if e <= a:
            answer += 1
            s,e = a,b
    return answer
def solution(N, stages):
    cnt = len(stages)
    dict = {}
    for i in range(1, N+1):
        if cnt == 0:
            dict[i] = 0
        else:
            num = stages.count(i)
            dict[i] = num / cnt
            cnt -= num
    answer = list(sorted(dict.items(), key = lambda x: (-x[1], x[0])))
    return [i[0] for i in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
from itertools import combinations

def solution(numbers):
    answer = []
    s = combinations(numbers,2)
    for i in s:
        a = sum(i)
        if a not in answer:
            answer.append(a)
    return sorted(answer)
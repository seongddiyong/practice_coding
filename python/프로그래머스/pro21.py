def solution(d, budget):
    d = list(sorted(d))
    while sum(d) > budget:
        d.pop()
    return len(d)

d = [2,2,3,3]
budget = 10
print(solution(d,budget))
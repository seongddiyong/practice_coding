def solution(lines):
    answer = 0
    temp = [0 for i in range(201)]
    for i in range(3):
        a,b = lines[i]
        for j in range(a+100,b+100):
                temp[j] += 1
    target = max(temp)
    if target == 3:
        answer = temp.count(target)
        answer += temp.count(target-1)
    elif target == 2:
        answer = temp.count(target)
    return answer

def solution2(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

lines = [[0, 5], [3, 9], [1, 10]]
print(solution2(lines))
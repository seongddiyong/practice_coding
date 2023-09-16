from itertools import permutations
def solution(n):
    answer = 0
    temp = []
    for _ in range(n):
        temp.append("(")
        temp.append(")")
    li = set(list(permutations(temp,n*2)))
    stack = []
    for i in li:
        cnt = n
        if i[0] == ")" or i[-1] == "(":
            continue
        for j in i:
            if j == "(":
                stack.append(j)
            elif j == ")" and len(stack) == 0:
                break
            elif j == ")" and len(stack) != 0:
                stack.pop()
                cnt -= 1
            if cnt == 0 and len(stack) == 0:
                answer += 1
    return answer

print(solution(2))
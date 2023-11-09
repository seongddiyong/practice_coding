def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        temp = list(skill[:])
        flag = True
        for j in i:
            if j in temp:
                if j == temp[0]:
                    temp.pop(0)
                else:
                    flag = False
                    break
            else:
                continue
        if flag:
            answer += 1
    return answer
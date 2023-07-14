def solution(a, b, c, d):
    answer = 0
    origin = [a,b,c,d]
    temp = list(set(origin))
    if len(temp) == 1:
        answer = 1111*temp[0]
    elif len(temp) == 2:
        if origin.count(temp[0]) == 3:
            answer = (10*temp[0]+temp[1])**2
        elif origin.count(temp[0]) == 2:
            answer = (temp[0]+temp[1]) * abs(temp[0]-temp[1])
        else:
            answer = (10*temp[1]+temp[0])**2
    elif len(temp) == 3:
        for i in temp:
            if [a,b,c,d].count(i) == 2:
                temp.remove(i)
                answer = temp[0]*temp[1]
    else:
        answer = min(temp)
    return answer

print(solution(4,1,4,4))
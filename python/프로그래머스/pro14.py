def solution(dartResult):
    answer = []
    temp = ""
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            if dartResult[i] == 'S':
                a = "**1"
            elif dartResult[i] == 'D':
                a = "**2"
            else:
                a = "**3"
            result = eval(temp + a)
            answer.append(result)
            temp = ""
        elif dartResult[i] == '*':
            if len(answer) <= 2:
                answer = [x*2 for x in answer]
            else:
                answer[1] *= 2
                answer[2] *= 2
        elif dartResult[i] == '#':
            answer[-1] *= -1
        else:
            temp += dartResult[i]
    return sum(answer)


def solution2(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)

print(solution2('1D2S#10S'))
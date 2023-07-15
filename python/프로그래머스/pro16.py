def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in completion:
        dict[i] -= 1
        if dict[i] == 0:
            del dict[i]
    answer = list(dict.keys())
    return answer[0]
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
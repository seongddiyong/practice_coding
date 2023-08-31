from itertools import combinations
from bisect import bisect_left

def make_case(x, infoDict):
    temp = x.split(" ")
    score = int(temp[-1])
    for i in range(5):
        for j in combinations(temp[:-1], i):
            key = "".join(j)
            if key in infoDict:
                infoDict[key].append(score)
            else:
                infoDict[key] = [score]


def find_answer(key, queryScore, infoDict):
    if key in infoDict:
        return len(infoDict[key]) - bisect_left(infoDict[key], queryScore)
    return 0

def solution(info, query):
    infoDict = dict()
    # 케이스 만들어주기
    for x in info:
        make_case(x, infoDict)
    # dict 내의 key를 기준으로 values 정렬
    for key in infoDict.keys():
        infoDict[key].sort()

    answer = []
    for x in query:
        tempArr = list(y for y in x.replace("and", " ").replace("-", "").split(" ") if len(y) > 0)
        queryScore = int(tempArr[-1])
        # 이진 탐색으로 queryScore보다 큰 점수들의 개수 반환
        if len(tempArr) == 1:
            answer.append(find_answer("", queryScore, infoDict))
        else:
            answer.append(find_answer("".join(tempArr[:-1]), queryScore, infoDict))
    
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))
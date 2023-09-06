import math
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = cnt2 = cnt3 = 0
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            cnt1 += 1
        if two[i%8] == answers[i]:
            cnt2 += 1
        if three[i%10] == answers[i]:
            cnt3 += 1
    temp = [cnt1, cnt2, cnt3]
    answer = []
    for k,i in enumerate(temp):
        if i == max(temp):
            answer.append(k+1)
    return answer
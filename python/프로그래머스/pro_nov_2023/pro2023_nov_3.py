def solution(s):
    s = s.replace('{{','').replace('},{','#').replace('}}','').split('#')
    s = sorted(s, key = lambda x: len(x))
    answer = []
    for i in s:
        temp = list(map(int, i.split(',')))
        for j in temp:
            if j not in answer:
                answer.append(j)
    return answer

from collections import Counter
def solution2(s):
    return [i[0] for i in Counter(list(map(int,s.replace('{{','').replace('},{',',').replace('}}','').split(',')))).most_common()]
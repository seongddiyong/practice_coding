from collections import deque
def solution(answers):
    temp = [0,0,0]
    a = deque([1,2,3,4,5])
    index_a = 0
    b = deque([1,2,3,4,5])
    index_b = 0
    c = deque([3,1,2,4,5])
    index_c = 0
    while index_a < len(answers):
        element = a.popleft()
        a.append(element)
        if element == answers[index_a]:
            temp[0] += 1
        index_a += 1
    while index_b < len(answers):
        if answers[index_b] == 2:
            temp[1] += 1
        index_b += 1
        if index_b == len(answers):
            break
        element = b.popleft()
        b.append(element)
        if element == answers[index_b]:
            temp[1] += 1
        index_b += 1  
    while index_c < len(answers):
        element = c.popleft()
        c.append(element)
        for _ in range(2):
            if element == answers[index_c]:
                temp[2] += 1
            index_c += 1
            if index_c == len(answers):
                break
    result = max(temp)
    answer = []
    for i in range(len(temp)):
        if result == temp[i]:
            answer.append(i+1)
    return answer
answers = [1,2,3,4,5]
print(solution(answers))
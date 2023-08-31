from collections import deque
def solution(numbers, direction):
    answer = deque(numbers)
    if direction == 'right':
        answer.appendleft(answer.pop())
    else:
        answer.append(answer.popleft())
    return list(answer)

print(solution([1,2,3],"right"))
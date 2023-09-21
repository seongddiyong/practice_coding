from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        r, i = queue.popleft()
        i += 1
        if i < n:
            queue.append([r+numbers[i], i])
            queue.append([r-numbers[i], i])
        else:
            if r == target:
                answer += 1
    return answer

def solution2(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution2(numbers, target))
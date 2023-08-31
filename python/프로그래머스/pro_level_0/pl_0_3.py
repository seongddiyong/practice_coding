def mysolution(numbers):
    answer = numbers[0]*numbers[1]
    while numbers:
        i = numbers.pop()
        for j in numbers:
            answer = max(answer,i * j)
    return answer

def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
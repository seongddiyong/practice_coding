def solution(num, total):
    answer = []
    if num % 2 == 0:
        A = total // (num // 2)
        start = (A - num + 1) // 2
        for i in range(num):
            answer.append(start+i)
    else:
        start = (total//num)-((num-1)//2)
        for i in range(num):
            answer.append(start+i)
    return answer

def solution2(num, total):
    if num % 2 == 1:
        return list(range(total//num-num//2, total//num+num//2+1))
    else:
        return list(range(total//num-num//2+1, total//num+num//2+1))
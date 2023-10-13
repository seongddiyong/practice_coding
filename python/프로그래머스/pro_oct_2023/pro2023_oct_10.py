from itertools import combinations
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
    	if n % i == 0:
        	return False
    return True
    
def solution(nums):
    answer = 0
    n = combinations(nums,3)
    for i in n:
        if isPrime(sum(i)):
            answer += 1
    return answer
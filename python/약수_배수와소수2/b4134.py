import math
import sys
input=sys.stdin.readline

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1
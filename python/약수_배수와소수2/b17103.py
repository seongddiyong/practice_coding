import sys
input = sys.stdin.readline

t = int(input())
# 에라토스테네스의 체
temp = [0,0] + [1 for _ in range(1000000)]
for i in range(2,1000000+1):
    if temp[i]:
        for j in range(i*2,1000000+1,i):
            temp[j] = 0 
for _ in range(t):
    n = int(input())
    result = 0
    for i in range(2,(n//2)+1):
        if temp[i] and temp[n-i]:
            result += 1
    print(result)
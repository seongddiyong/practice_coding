import sys
input = sys.stdin.readline

n = int(input())
i,result = 1,0
while i*i <= n:
    i += 1
print(i-1)


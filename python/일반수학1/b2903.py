#중앙 이동 알고리즘

n = int(input())
i,result = 0,0
past = 2
for i in range(1,n+1):
    past += 2**(i-1)
    result = past**2

print(result)
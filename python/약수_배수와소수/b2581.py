from sys import stdin
input = stdin.readline

m = int(input())
n = int(input())
result = []
for i in range(m,n+1):
    if i == 1:
        pass
    temp = 0
    for k in range(2,i):
        if i%k == 0:
            temp += 1
            break
    if temp == 0:
        result.append(i)
if len(result)==0:
    print("-1")
else:
    print(sum(result))
    print(min(result))
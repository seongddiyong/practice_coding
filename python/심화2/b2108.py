import sys
input = sys.stdin.readline

n = int(input())
temp = sorted([int(input()) for _ in range(n)])

print(round(sum(temp)/n))

print(temp[len(temp)//2])

dic = {}
for i in temp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values())
cnt = []

for i in dic:
    if mx == dic[i]:
        cnt.append(i)
if len(cnt)>1:
    print(cnt[1])
else:
    print(cnt[0])

print(temp[-1]-temp[0])
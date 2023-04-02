from sys import stdin
input = stdin.readline
li = [list(map(int, input().split())) for i in range(9)]

temp = []
res = []
for _ in range(9):
    maxi = max(li[_])
    res.append(maxi)
    temp.append(li[_].index(maxi))

print(max(res))
print(res.index(max(res))+1, temp[res.index(max(res))]+1)
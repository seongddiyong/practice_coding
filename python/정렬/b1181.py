from sys import stdin
input = stdin.readline

n = int(input())
temp = [input().rstrip() for _ in range(n)]
temp1 = list(set(temp))
sort_wd = []
for i in temp1:
    sort_wd.append((len(i),i))  #튜플 집어넣기
result = sorted(sort_wd)
for _,i in result:
    print(i)
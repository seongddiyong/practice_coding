from sys import stdin
input = stdin.readline

n = int(input())
temp = []
for _ in range(n):
    age, name = map(str,input().split())
    age = int(age)
    temp.append((age,name))
temp.sort(key = lambda x:x[0])
for i in temp:
    print(i[0],i[1])
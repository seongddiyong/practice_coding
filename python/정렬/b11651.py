from sys import stdin
input = stdin.readline

n = int(input())
temp = [list(map(int,input().split())) for _ in range(n)]
temp.sort(key=lambda x: (x[1],x[0]))
for i in temp:
    print(i[0],i[1])
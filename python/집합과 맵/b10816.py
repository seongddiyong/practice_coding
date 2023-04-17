import sys
input = sys.stdin.readline

n = int(input())
num = map(int,input().split())
m = int(input())
check = map(int,input().split())
dict = {}
for i in num:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in check:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')
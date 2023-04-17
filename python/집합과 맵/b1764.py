import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}
for i in range(n):
    hear = input().rstrip()
    dict[hear] = 1
for i in range(m):
    see = input().rstrip()
    if see in dict:
        dict[see] += 1
dict = {key:value for key,value in dict.items() if value == 2}
dict = sorted(dict)
print(len(dict))
for i in dict:
    print(i)

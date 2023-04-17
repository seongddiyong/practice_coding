import sys
input = sys.stdin.readline

n = int(input())
temp = {}
for i in range(n):
    person, status = input().split()
    if person not in temp:
        temp[person] = status
    else:
        del temp[person]
temp1 = sorted(temp.keys(), reverse=True)
for i in temp1:
    print(i)

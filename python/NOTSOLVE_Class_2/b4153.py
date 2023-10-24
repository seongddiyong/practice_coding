from sys import stdin
input = stdin.readline
while True:
    t = list(map(int, input().split()))
    if 0 in t:
        break
    t.sort()
    if t[0]**2 + t[1]**2 == t[2]**2:
        print("right")
    else:
        print("wrong")
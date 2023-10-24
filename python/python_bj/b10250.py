from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    stair = (n%h)*100
    num = n//h + 1
    if stair == 0:
        stair = h*100
        num -= 1
    print(stair+num)